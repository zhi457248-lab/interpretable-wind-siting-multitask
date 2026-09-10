# Data sources and provenance

This file lists the third-party data sources used to construct the derived dataset. None of the raw data are redistributed here; the table below records where they were downloaded from and the exact extract window.

| Source | Type | Coverage | Extract window | URL |
|---|---|---|---|---|
| ERA5-Land hourly reanalysis | Meteorological (wind speed at 100 m, density, temperature) | Mainland China | 2010–2023 | https://cds.climate.copernicus.eu/ |
| SRTM DEM v3 | Elevation, slope, aspect | Mainland China tiles | static | https://earthexplorer.usgs.gov/ |
| ESA WorldCover 10 m | Land-use mask (10 m resolution aggregated to 0.01°) | Mainland China | 2020 | https://worldcover2020.esa.int/ |
| OpenStreetMap | Roads, settlements, water bodies | Mainland China | 2024 | https://www.openstreetmap.org/ |
| China provincial power-grid GIS (State Grid public map) | Grid distance, substation locations | Mainland China | 2024 | https://www.sgcc.com.cn/ |
| China protected-area shapefile (MEE ecological red lines) | Exclusion zones | Mainland China | 2023 | http://www.mee.gov.cn/ |

For each source, the construction pipeline in `src/data/build_dataset.py` records the exact snapshot date and the SHA256 of the downloaded archive in `data/snapshots.sha256` (to be populated at release time).