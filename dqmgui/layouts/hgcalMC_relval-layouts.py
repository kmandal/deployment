

def hgcaldigisVlayout(i, p, *rows): i[p] = DQMItem(layout=rows)
hgcaldigisVlayout(dqmitems, 'MCLayouts/HGcal/HGcalDigis/00 EE DigiOccupancy_Minus_layer_27',[{'path' : 'HGCalDigiV/HGCalEESensitive/DigiOccupancy_Minus_layer_27'}])
hgcaldigisVlayout(dqmitems, 'MCLayouts/HGcal/HGcalDigis/01 FH DigiOccupancy_Minus_layer_11',[{'path' : 'HGCalDigiV/HGCalHESiliconSensitive/DigiOccupancy_Minus_layer_11'}])
hgcaldigisVlayout(dqmitems, 'MCLayouts/HGcal/HGcalDigis/02 BH DigiOccupancy_Minus_layer_11',[{'path' : 'HGCalDigiV/HCal/DigiOccupancy_Minus_layer_11'}])

def hgcalrechitVlayout(i, p, *rows): i[p] = DQMItem(layout=rows)
hgcalrechitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalRecHits/00 EE HitOccupancy_Plus_layer_27',[{'path' : 'HGCalRecHitsV/HGCalEESensitive/HitOccupancy_Plus_layer_27'}])
hgcalrechitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalRecHits/01 FH HitOccupancy_Plus_layer_11',[{'path' : 'HGCalRecHitsV/HGCalHESiliconSensitive/HitOccupancy_Plus_layer_11'}])
hgcalrechitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalRecHits/02 BH HitOccupancy_Plus_layer_11',[{'path' : 'HGCalRecHitsV/HCal/HitOccupancy_Plus_layer_11'}])

def hgcalsimhitVlayout(i, p, *rows): i[p] = DQMItem(layout=rows)
hgcalsimhitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalSimHits/00 EE HitOccupancy_Minus_layer_27',[{'path' : 'HGCalSimHitsV/HGCalEESensitive/HitOccupancy_Minus_layer_27'}])
hgcalsimhitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalSimHits/01 FH HitOccupancy_Minus_layer_11',[{'path' : 'HGCalSimHitsV/HGCalHESiliconSensitive/HitOccupancy_Minus_layer_11'}])
hgcalsimhitVlayout(dqmitems, 'MCLayouts/HGcal/HGcalSimHits/02 BH HitOccupancy_Minus_layer_11',[{'path' : 'HGCalSimHitsV/HCal/HitOccupancy_Minus_layer_11'}])

def hgcalhitcalibrationlayout(i, p, *rows): i[p] = DQMItem(layout=rows)
hgcalhitcalibrationlayout(dqmitems, 'MCLayouts/HGcal/HitCalibration/00 LayerOccupancy',[{'path' : 'HGCalHitCalibration/LayerOccupancy'}])





