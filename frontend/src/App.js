import React, { useState, useEffect } from 'react';
import { Container, Grid, Paper, Tabs, Tab, Box } from '@mui/material';
import RegionSelector from './components/RegionSelector';
import PlotDisplay from './components/PlotDisplay';
import TabPanel from './components/TabPanel';
import axios from 'axios';

function App() {
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState('');
  const [plotData, setPlotData] = useState({});
  const [tabValue, setTabValue] = useState(0);

  useEffect(() => {
    axios.get('http://localhost:8000/regions').then((response) => {
      setRegions(response.data);
      setSelectedRegion(response.data[0]);
    });
  }, []);

  useEffect(() => {
    if (selectedRegion) {
      axios.get(`http://localhost:8000/region/${selectedRegion}`).then((response) => {
        setPlotData(response.data.plots);
        // Reset tab to 0 if current tab is not available for 'Across the UK'
        if (selectedRegion === 'Across the UK' && tabValue > 1) {
          setTabValue(0);
        }
      });
    }
  }, [selectedRegion]);

  const handleRegionChange = (event) => {
    setSelectedRegion(event.target.value);
  };

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  return (
    <Container maxWidth="lg">
      <h1>UK House Price Analysis</h1>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <RegionSelector
            regions={regions}
            selectedRegion={selectedRegion}
            onRegionChange={handleRegionChange}
          />
        </Grid>
        <Grid item xs={12}>
          <Paper>
            <Tabs
              value={tabValue}
              onChange={handleTabChange}
              indicatorColor="primary"
              textColor="primary"
              centered
            >
              <Tab label="Average Price" />
              <Tab label="Cumulative Change" />
              <Tab 
                label="Property Type" 
                disabled={selectedRegion === 'Across the UK'}
              />
              <Tab 
                label="Property Type Change" 
                disabled={selectedRegion === 'Across the UK'}
              />
            </Tabs>
            <Box sx={{ p: 3 }}>
              <TabPanel value={tabValue} index={0}>
                <PlotDisplay plotData={plotData.average_price} />
              </TabPanel>
              <TabPanel value={tabValue} index={1}>
                <PlotDisplay plotData={plotData.cumulative_change} />
              </TabPanel>
              <TabPanel value={tabValue} index={2}>
                {selectedRegion !== 'Across the UK' && plotData.property_type ? (
                  <PlotDisplay plotData={plotData.property_type} />
                ) : (
                  <div>Property type data not available for UK-wide view</div>
                )}
              </TabPanel>
              <TabPanel value={tabValue} index={3}>
                {selectedRegion !== 'Across the UK' && plotData.property_type_change ? (
                  <PlotDisplay plotData={plotData.property_type_change} />
                ) : (
                  <div>Property type change data not available for UK-wide view</div>
                )}
              </TabPanel>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}

export default App;