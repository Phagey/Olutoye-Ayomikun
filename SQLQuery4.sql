--Cleaning Data in SQL Queries

Select *
from Portfolio.dbo.NashvilleHousingData


--To Standardize the Date Format

Select SaleDateConverted, CONVERT(Date,SaleDate)
from Portfolio.dbo.NashvilleHousingData


UPDATE NashvilleHousingData
Set SaleDate IN CONVERT(Date,SaleDate)


ALTER TABLE NashvilleHousingData
Add SaleDateConverted Date;

UPDATE NashvilleHousingData
Set SaleDateConverted = CONVERT(Date,SaleDate)



--To Populate Property Address Data


Select *
from Portfolio.dbo.NashvilleHousingData
--where PropertyAddress is null
Order by ParcelID



Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress,ISNULL(a.PropertyAddress, b.PropertyAddress)
from Portfolio.dbo.NashvilleHousingData a
join Portfolio.dbo.NashvilleHousingData b
	on a.ParcelID = b.ParcelID
	AND a.UniqueID <> b.UniqueID
where a.PropertyAddress is null


Update a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
from Portfolio.dbo.NashvilleHousingData a
join Portfolio.dbo.NashvilleHousingData b
	on a.ParcelID = b.ParcelID
	AND a.UniqueID <> b.UniqueID
where a.PropertyAddress is null



--Breaking out Addresses into Individual Columns(Adress,City,State)

Select PropertyAddress
from Portfolio.dbo.NashvilleHousingData
--where PropertyAddress is null
--Order by ParcelID

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) as Address

from Portfolio.dbo.NashvilleHousingData



ALTER TABLE NashvilleHousingData
Add PropertySplitAddress Nvarchar(255);

UPDATE NashvilleHousingData
Set PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)


ALTER TABLE NashvilleHousingData
Add PropertySplitCity NVARCHAR(255);

UPDATE NashvilleHousingData
Set PropertySplitCity =  SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))


select *
from Portfolio.dbo.NashvilleHousingData




select 
PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)
 ,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)
 ,PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)
From Portfolio.dbo.NashvilleHousingData


ALTER TABLE NashvilleHousingData
Add OwnerSplitAddress Nvarchar(255);

UPDATE NashvilleHousingData
Set OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 3)


ALTER TABLE NashvilleHousingData
Add OwnerSplitCity NVARCHAR(255);

UPDATE NashvilleHousingData
Set OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'), 2)


ALTER TABLE NashvilleHousingData
Add OwnerSplitState NVARCHAR(255);

UPDATE NashvilleHousingData
Set OwnerSplitState =  PARSENAME(REPLACE(OwnerAddress, ',', '.'), 1)


select *
from Portfolio.dbo.NashvilleHousingData



--To change Y and N to Yes and NO in "Sold as vacant field"

Select Distinct(SoldAsVacant), Count(SoldAsVacant)
from Portfolio.dbo.NashvilleHousingData
Group by SoldAsVacant
Order by 2


Select SoldAsVacant
, CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
       ELSE SoldAsVacant
       END
from Portfolio.dbo.NashvilleHousingData


Update NashvilleHousingData
Set SoldAsVacant = CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
       ELSE SoldAsVacant
       END




-- To Remove Duplicates

WITH RowNumCTE AS (
Select *,
     ROW_NUMBER() OVER (
	 PARTITION BY ParcelID,
				  PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  ORDER BY
					 UniqueID
					 ) row_num

from Portfolio.dbo.NashvilleHousingData
--Order By ParcelID
)

Select *
From RowNumCTE
Where row_num > 1
Order by PropertyAddress




--To delete unused Columns


select *
from Portfolio.dbo.NashvilleHousingData

ALTER TABLE Portfolio.dbo.NashvilleHousingData
DROP Column OwnerAddress, TaxDistrict, PropertyAddress

ALTER TABLE Portfolio.dbo.NashvilleHousingData
DROP Column Saledate