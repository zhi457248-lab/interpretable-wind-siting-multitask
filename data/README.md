# Data availability statement

## Public datasets (used as-is)

| Dataset | Source | Licence | Citation |
|---|---|---|---|
| ERA5 reanalysis | Copernicus Climate Data Store | Copernicus Licence (free, attribution) | Hersbach et al. 2020, *Q. J. R. Meteorol. Soc.* 146:1999–2049 |
| OpenStreetMap tiles | https://www.openstreetmap.org | ODbL 1.0 | ODbL contributors |
| GB/T 19963 | National Standards of the People's Republic of China | Public standard | GB/T 19963-2021 |
| Chinese-BERT-wwm | HIT-iFLYTEK Joint Lab | Apache 2.0 | Cui et al. 2021 |

## Internal / commercial datasets (not redistributed)

- **SCADA traces** for the nine wind-farm validation sites: aggregated, anonymised
  summary statistics are released in this repository. Raw turbine-level
  SCADA traces are **not** redistributed due to commercial confidentiality
  with the operating utilities. Please contact the corresponding author
  for collaboration requests.
- **Internal feature engineering tables** (slope, aspect, roughness class):
  derived from SRTM DEM at 30 m resolution; intermediate raster products
  not redistributed to limit repository size. Final 0.25°-grid features
  used in the manuscript are released.

## Policy corpus (81 documents)

The 81 policy documents comprise national, provincial, and municipal
energy-policy documents from official government websites. Each document
is publicly retrievable; see Appendix A of the manuscript for the full
list with URLs.

## Reproduction of derived artefacts

The following derived artefacts **are** released in this repository:

- `paper_revised.tex` and `paper_revised.pdf` — full manuscript source
- `*.png` figures — all figures referenced in the manuscript
- `paper/figures/` — same figures organised for portability
- `requirements.txt` and `environment.yml` — software environment
- `src/` — implementation skeleton with module-level documentation

The following derived artefacts are **withheld** at the submission stage
to preserve anonymised peer review and will be released upon acceptance:

- Trained model checkpoints (PyTorch `.pt` files)
- Tokenised policy corpus (HuggingFace `datasets` format)
- Final 0.25°-grid feature tensors (`.npz` format)
- Per-province cross-validation predictions (CSV)

## Statement template (for inclusion in the manuscript)

> *The ERA5 reanalysis, OpenStreetMap, and Chinese-BERT-wwm components
> of this work are publicly available under their respective licences
> (Copernicus, ODbL, Apache 2.0). Aggregated SCADA summary statistics
> are released alongside this repository; raw turbine-level SCADA traces
> are not redistributed due to commercial confidentiality and can be
> requested from the corresponding author under a data-use agreement.
> A Zenodo DOI will accompany the full reproducibility release upon
> acceptance.*