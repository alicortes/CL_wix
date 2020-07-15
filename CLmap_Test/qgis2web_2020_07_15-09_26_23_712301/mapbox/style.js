
var styleJSON = {
    "version": 8,
    "name": "qgis2web export",
    "pitch": 0,
    "light": {
        "intensity": 0.2
    },
    "sources": {
        "Background_0": {
            "type": "raster",
            "tiles": ["http://a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png"],
            "tileSize": 256
        },
        "LakeCountyBoundary_1": {
            "type": "geojson",
            "data": json_LakeCountyBoundary_1
        }
                    ,
        "Tributaries_2": {
            "type": "geojson",
            "data": json_Tributaries_2
        }
                    ,
        "LakeBathymetry_3": {
            "type": "geojson",
            "data": json_LakeBathymetry_3
        }
                    ,
        "MetStation_4": {
            "type": "geojson",
            "data": json_MetStation_4
        }
                    ,
        "SurfaceTemperature_5": {
            "type": "geojson",
            "data": json_SurfaceTemperature_5
        }
                    ,
        "StreamMonitoringSite_6": {
            "type": "geojson",
            "data": json_StreamMonitoringSite_6
        }
                    ,
        "Thermistorchain_7": {
            "type": "geojson",
            "data": json_Thermistorchain_7
        }
                    },
    "sprite": "",
    "glyphs": "https://glfonts.lukasmartinelli.ch/fonts/{fontstack}/{range}.pbf",
    "layers": [
        {
            "id": "background",
            "type": "background",
            "layout": {},
            "paint": {
                "background-color": "#ffffff"
            }
        },
        {
            "id": "lyr_Background_0_0",
            "type": "raster",
            "source": "Background_0"
        },
        {
            "id": "lyr_LakeCountyBoundary_1_0",
            "type": "line",
            "source": "LakeCountyBoundary_1",
            "layout": {},
            "paint": {'line-width': 2.0, 'line-opacity': 1.0, 'line-color': '#000000'}
        }
,
        {
            "id": "lyr_Tributaries_2_0",
            "type": "line",
            "source": "Tributaries_2",
            "layout": {},
            "paint": {'line-width': 1.6428571428571428, 'line-opacity': 1.0, 'line-color': '#1a49d4'}
        }
,
        {
            "id": "lyr_LakeBathymetry_3_0",
            "type": "line",
            "source": "LakeBathymetry_3",
            "layout": {},
            "paint": {'line-width': 0.9285714285714285, 'line-opacity': 1.0, 'line-color': '#626459'}
        }
,
        {
            "id": "lyr_LakeBathymetry_3_1",
            "type": "symbol",
            "source": "LakeBathymetry_3",
            "layout": {'text-offset': 0.0, 'text-field': None, 'text-size': '10.085714285714284', 'text-font': ['Open Sans Regular']},
            "paint": {'text-halo-width': '3.571428571428571', 'text-halo-color': '#ffffff', 'text-color': '#000000'}
        }
,
        {
            "id": "lyr_MetStation_4_0",
            "type": "circle",
            "source": "MetStation_4",
            "layout": {},
            "paint": {'circle-radius': ['/', 15.0, 2], 'circle-color': '#8940e2', 'circle-opacity': 1.0, 'circle-stroke-width': 1.4285714285714286, 'circle-stroke-color': '#0f1319'}
        }
,
        {
            "id": "lyr_SurfaceTemperature_5_0",
            "type": "circle",
            "source": "SurfaceTemperature_5",
            "layout": {},
            "paint": {'circle-radius': ['/', 10.714285714285714, 2], 'circle-color': '#eff6fe', 'circle-opacity': 1.0, 'circle-stroke-width': 1.4285714285714286, 'circle-stroke-color': '#05080c'}
        }
,
        {
            "id": "lyr_StreamMonitoringSite_6_0",
            "type": "circle",
            "source": "StreamMonitoringSite_6",
            "layout": {},
            "paint": {'circle-radius': ['/', 14.285714285714285, 2], 'circle-color': '#5bf613', 'circle-opacity': 1.0, 'circle-stroke-width': 1, 'circle-stroke-color': '#232323'}
        }
,
        {
            "id": "lyr_Thermistorchain_7_0",
            "type": "circle",
            "source": "Thermistorchain_7",
            "layout": {},
            "paint": {'circle-radius': ['/', 13.57142857142857, 2], 'circle-color': '#f20a0a', 'circle-opacity': 1.0, 'circle-stroke-width': 0.7142857142857143, 'circle-stroke-color': '#000000'}
        }
],
}