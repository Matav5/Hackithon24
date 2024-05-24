#Zde by měly být funkce a pomocné funkce na vizualizaci grafů
import plotly.graph_objects as go
import plotly.express as px
import json
import pandas as pd
import numpy as np
import os 
def mapa():
  
    with open('C:\\Users\\Matav\\Documents\\Github\\Template\\app\\data\\kraje\\kraje_polygony.geojson', 'r', encoding='utf-8',errors='ignore') as f:
        geojson = json.load(f)
        
        """     
{
    "type": "FeatureCollection",
    "name": "Ložiska nerostných surovin a prognózní zdroje",
    "iri": "https://registry.geology.cz/od/loziska_zdroje_ner_sur",
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "vytvoreno": {
        "typ": "Časový okamžik",
        "datum": "19.05.2024"
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "klic": "3043700",
                "iri": "https://registry.geology.cz/od/loziska_zdroje_ner_sur/3043700",
                "cislo_suris": "304370000",
                "subregistr": "B - Výhradní ložisko",
                "nazev": "Horní Hutě-Čeřínek",
                "surovina": "Kámen pro hrubou a ušlechtilou kamenickou výrobu",
                "charakteristika_suroviny": "žula",
                "tezba": "dřívější povrchová",
                "organizace": "KAVEX - GRANIT HOLDING a. s.",
                "ico": "25183435"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            15.43099827,
                            49.37279121
                        ],
                        [
                            15.42985555,
                            49.37069628
                        ],
                        [
                            15.43000248,
                            49.37072629
                        ],
                        [
                            15.43003659,
                            49.37069281
                        ],
                        [
                            15.42995097,
                            49.37055902
                        ],
                        [
                            15.42988941,
                            49.3705178
                        ],
                        [
                            15.42982447,
                            49.37049442
                        ],
                        [
                            15.43350048,
                            49.36976792
                        ],
                        [
                            15.43346255,
                            49.37055315
                        ],
                        [
                            15.43352849,
                            49.37115651
                        ],
                        [
                            15.43350241,
                            49.37187928
                        ],
                        [
                            15.43260473,
                            49.37331984
                        ],
                        [
                            15.43099827,
                            49.37279121
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "klic": "3043800",
                "iri": "https://registry.geology.cz/od/loziska_zdroje_ner_sur/3043800",
                "cislo_suris": "304380001",
                "subregistr": "B - Výhradní ložisko",
                "nazev": "Boršov",
                "surovina": "Kámen pro hrubou a ušlechtilou kamenickou výrobu",
                "charakteristika_suroviny": "žula",
                "tezba": "dřívější povrchová",
                "organizace": "KAVEX - GRANIT HOLDING a. s.",
                "ico": "25183435"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            15.42303906,
                            49.39110278
                        ],
                        [
                            15.42358852,
                            49.39062171
                        ],
                        [
                            15.42479407,
                            49.39012125
                        ],
                        [
                            15.42628748,
                            49.39015149
                        ],
                        [
                            15.42690698,
                            49.3907634
                        ],
                        [
                            15.42652217,
                            49.39162024
                        ],
                        [
                            15.42571398,
                            49.3916364
                        ],
                        [
                            15.42303906,
                            49.39110278
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "klic": "3043800",
                "iri": "https://registry.geology.cz/od/loziska_zdroje_ner_sur/3043800",
                "cislo_suris": "304380002",
                "subregistr": "B - Výhradní ložisko",
                "nazev": "Boršov",
                "surovina": "Kámen pro hrubou a ušlechtilou kamenickou výrobu",
                "charakteristika_suroviny": "žula",
                "tezba": "dřívější povrchová",
                "organizace": "KAVEX - GRANIT HOLDING a. s.",
                "ico": "25183435"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            15.43020735,
                            49.39648507
                        ],
                        [
                            15.43015593,
                            49.3963903
                        ],
                        [
                            15.42999331,
                            49.39622311
                        ],
                        [
                            15.42987849,
                            49.39602354
                        ],
                        [
                            15.42979609,
                            49.39579942
                        ],
                        [
                            15.42990512,
                            49.39559077
                        ],
                        [
                            15.42985842,
                            49.39525174
                        ],
                        [
                            15.42981039,
                            49.39513913
                        ],
                        [
                            15.42995026,
                            49.39498734
                        ],
                        [
                            15.42990211,
                            49.39480223
                        ],
                        [
                            15.43006956,
                            49.39479765
                        ],
                        [
                            15.43015802,
                            49.39455109
                        ],
                        [
                            15.43096395,
                            49.39418134
                        ],
                        [
                            15.43198525,
                            49.39384712
                        ],
                        [
                            15.43330649,
                            49.39405362
                        ],
                        [
                            15.43349006,
                            49.3944762
                        ],
                        [
                            15.43309517,
                            49.39538661
                        ],
                        [
                            15.43259065,
                            49.39614318
                        ],
                        [
                            15.43214647,
                            49.396216
                        ],
                        [
                            15.4314886,
                            49.39624436
                        ],
                        [
                            15.43090939,
                            49.39629719
                        ],
                        [
                            15.43020735,
                            49.39648507
                        ]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "klic": "3043900",
                "iri": "https://registry.geology.cz/od/loziska_zdroje_ner_sur/3043900",
                "cislo_suris": "304390000",
                "subregistr": "B - Výhradní ložisko",
                "nazev": "Řeka",
                "surovina": "Kámen pro hrubou a ušlechtilou kamenickou výrobu",
                "charakteristika_suroviny": "pískovec",
                "tezba": "současná povrchová",
                "organizace": "Slezské kamenolomy a.s.",
                "ico": "08300283"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            18.571136,
                            49.64652422
                        ],
                        [
                            18.5696734,
                            49.64710494
                        ],
                        [
                            18.56791379,
                            49.64475598
                        ],
                        [
                            18.56789886,
                            49.64476421
                        ],
                        [
                            18.56710984,
                            49.64353141
                        ],
                        [
                            18.56924151,
                            49.64293222
                        ],
                        [
                            18.56944873,
                            49.6430515
                        ],
                        [
                            18.5696469,
                            49.64324247
                        ],
                        [
                            18.56973716,
                            49.64351791
                        ],
                        [
                            18.56979734,
                            49.64370153
                        ],
                        [
                            18.57002198,
                            49.64390294
                        ],
                        [
                            18.57002311,
                            49.64389397
                        ],
                        [
                            18.57033168,
                            49.64409082
                        ],
                        [
                            18.57070812,
                            49.6443003
                        ],
                        [
                            18.57092213,
                            49.64436581
                        ],
                        [
                            18.5709486,
                            49.64437624
                        ],
                        [
                            18.57107144,
                            49.64428354
                        ],
                        [
                            18.571136,
                            49.64652422
                        ]
                    ]
                ]
            }
        }
    ]
}
    """
    df = pd.DataFrame({
       "kraj": [feature["properties"]["naz_cznuts3"] for feature in geojson["features"]],
        "pocet_ob_91": [feature["properties"]["pocet_ob_91"] for feature in geojson["features"]]
    }
    )
    print(df.head())
    fig = px.choropleth_mapbox(data_frame=df, locations="kraj",featureidkey="properties.naz_cznuts3",geojson=geojson,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 49.37279121, "lon": 15.43099827},hover_name="kraj", hover_data=["pocet_ob_91"])
    return fig
