ol.proj.proj4.register(proj4);
ol.proj.get("EPSG:3857").setExtent([-13697820.742142, 4705322.165229, -13634401.994786, 4752771.058530]);
var wms_layers = [];


        var lyr_Background_0 = new ol.layer.Tile({
            'title': 'Background',
            'type': 'base',
            'opacity': 0.800000,
            
            
            source: new ol.source.XYZ({
    attributions: ' ',
                url: 'http://a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png'
            })
        });
var format_LakeCountyBoundary_1 = new ol.format.GeoJSON();
var features_LakeCountyBoundary_1 = format_LakeCountyBoundary_1.readFeatures(json_LakeCountyBoundary_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_LakeCountyBoundary_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_LakeCountyBoundary_1.addFeatures(features_LakeCountyBoundary_1);
var lyr_LakeCountyBoundary_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_LakeCountyBoundary_1, 
                style: style_LakeCountyBoundary_1,
                interactive: true,
                title: '<img src="styles/legend/LakeCountyBoundary_1.png" /> Lake County Boundary'
            });
var format_CL_Monitoring_Sites_2 = new ol.format.GeoJSON();
var features_CL_Monitoring_Sites_2 = format_CL_Monitoring_Sites_2.readFeatures(json_CL_Monitoring_Sites_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_CL_Monitoring_Sites_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_CL_Monitoring_Sites_2.addFeatures(features_CL_Monitoring_Sites_2);
var lyr_CL_Monitoring_Sites_2 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_CL_Monitoring_Sites_2, 
                style: style_CL_Monitoring_Sites_2,
                interactive: true,
    title: 'CL_Monitoring_Sites<br />\
    <img src="styles/legend/CL_Monitoring_Sites_2_0.png" /> Met<br />\
    <img src="styles/legend/CL_Monitoring_Sites_2_1.png" /> Stream<br />\
    <img src="styles/legend/CL_Monitoring_Sites_2_2.png" /> Surface<br />\
    <img src="styles/legend/CL_Monitoring_Sites_2_3.png" /> Tchain<br />'
        });

lyr_Background_0.setVisible(true);lyr_LakeCountyBoundary_1.setVisible(true);lyr_CL_Monitoring_Sites_2.setVisible(true);
var layersList = [lyr_Background_0,lyr_LakeCountyBoundary_1,lyr_CL_Monitoring_Sites_2];
lyr_LakeCountyBoundary_1.set('fieldAliases', {'Id': 'Id', 'Area': 'Area', });
lyr_CL_Monitoring_Sites_2.set('fieldAliases', {'Category': 'Category', 'Status': 'Status', 'Site ID': 'Site ID', 'Img_Field': 'Img_Field', });
lyr_LakeCountyBoundary_1.set('fieldImages', {'Id': 'Range', 'Area': 'TextEdit', });
lyr_CL_Monitoring_Sites_2.set('fieldImages', {'Category': 'TextEdit', 'Status': 'TextEdit', 'Site ID': 'TextEdit', 'Img_Field': 'TextEdit', });
lyr_LakeCountyBoundary_1.set('fieldLabels', {'Id': 'no label', 'Area': 'no label', });
lyr_CL_Monitoring_Sites_2.set('fieldLabels', {'Category': 'inline label', 'Status': 'inline label', 'Site ID': 'inline label', 'Img_Field': 'no label', });
lyr_CL_Monitoring_Sites_2.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});