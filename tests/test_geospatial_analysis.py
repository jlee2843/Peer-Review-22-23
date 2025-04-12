import geopandas as gpd
import pandas as pd

from pipeline.geospatial_analysis import GeospatialAnalysis


def test_merge_geo(tmp_path):
    gdf = gpd.GeoDataFrame({'region': ['A', 'B'], 'geometry': [None, None]})
    shapefile_path = tmp_path / "regions.shp"
    gdf.to_file(shapefile_path)
    df = pd.DataFrame({'region': ['A', 'B'], 'value': [10, 20]})
    analysis = GeospatialAnalysis(df, shapefile_path, 'region', 'value')
    merged = analysis.aggregate_and_merge()
    assert 'value' in merged.columns
