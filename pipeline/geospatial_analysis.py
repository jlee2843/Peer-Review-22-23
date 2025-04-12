import geopandas as gpd


class GeospatialAnalysis:
    def __init__(self, df, shapefile, region_col, value_col):
        self.df = df
        self.shapefile = shapefile
        self.region_col = region_col
        self.value_col = value_col

    def aggregate_and_merge(self):
        gdf = gpd.read_file(self.shapefile)
        region_means = self.df.groupby(self.region_col)[self.value_col].mean().reset_index()
        return gdf.merge(region_means, on=self.region_col)
