select *
from Portfolio..CovidDeaths
where continent is not null
order by 3,4


--select *
--from Portfolio..CovidVaccinations
--order by 3,4


--to select the data that we will be using

Select location, date, total_cases, new_cases, total_deaths, population
from Portfolio..CovidDeaths
where continent is not null
order by 1,2

--Now we look at Total_Cases vs Total_Deaths
--which shows the likelihood of dying if covid is contracted in any of the listed countries

Select location, date, total_cases,total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from Portfolio..CovidDeaths
where location like '%states%'
and continent is not null
order by 1,2


--Now we look at the Total Cases vs Population
--To show what percentage of Population got covid

Select location, date, Population, total_cases, (total_cases/Population)*100 as PercentOfInfectedPopulation
from Portfolio..CovidDeaths
--where location like '%states%'
where continent is not null
order by 1,2


--Looking at Countries with highest infection rate compared to Population

Select location, Population, MAX(total_cases) as Highest_Infection_Count, MAX((total_cases/Population))*100 as PercentOfInfectedPopulation
from Portfolio..CovidDeaths
--where location like '%states%'
Group by location, Population
order by PercentOfInfectedPopulation desc


--To show countries with the highest death count per population

Select location, MAX(cast(Total_deaths as int)) as TotalDeathCount
from Portfolio..CovidDeaths
--where location like '%states%'
where continent is not null
Group by location
order by TotalDeathCount desc


--To break things down by continent

--Now to show continents witht the highest death count per population

Select continent, MAX(cast(Total_deaths as int)) as TotalDeathCount
from Portfolio..CovidDeaths
--where location like '%states%'
where continent is not null
Group by continent
order by TotalDeathCount desc


--GLOBAL NUMBERS

SELECT
  SUM(new_cases) AS TotalCases,
  SUM(CAST(new_deaths AS INT)) AS TotalDeaths,
  CASE
    WHEN SUM(new_cases) = 0 THEN NULL
    ELSE SUM(CAST(new_deaths AS INT)) * 100.0 / NULLIF(SUM(new_cases), 0)
  END AS DeathPercentage
FROM
  Portfolio..CovidDeaths
WHERE
  continent IS NOT NULL
--GROUP BY
--  date
ORDER BY
  DeathPercentage desc;


  --Looking at Total Vaccination vs Population

  SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
       SUM(CAST(vac.new_vaccinations AS BIGINT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM portfolio..CovidDeaths dea
JOIN portfolio..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY 2,3



--Use CTE

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations,  RollingPeopleVaccinated)
as
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
       SUM(CAST(vac.new_vaccinations AS BIGINT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM portfolio..CovidDeaths dea
JOIN portfolio..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
--ORDER BY 2,3
)
select *, (RollingPeopleVaccinated/Population)*100
from PopvsVac



--TEMP TABLE

DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
       SUM(CAST(vac.new_vaccinations AS BIGINT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM portfolio..CovidDeaths dea
JOIN portfolio..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
--WHERE dea.continent IS NOT NULL
--ORDER BY 2,3

select *, (RollingPeopleVaccinated/Population)*100
from #PercentPopulationVaccinated


-- Creating view to store data for later visualizations

CREATE VIEW NewViewName AS
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, 
       SUM(CAST(vac.new_vaccinations AS BIGINT)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) AS RollingPeopleVaccinated
FROM portfolio..CovidDeaths dea
JOIN portfolio..CovidVaccinations vac
    ON dea.location = vac.location
    AND dea.date = vac.date
WHERE dea.continent IS NOT NULL;


DROP VIEW NewViewName;