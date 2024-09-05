import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, AppBar, Tabs, Tab, Box, styled } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import RegionSelector from './components/RegionSelector';
import PlotDisplay from './components/PlotDisplay';
import TabPanel from './components/TabPanel';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#f50057',
    },
  },
});

const StyledTabs = styled(Tabs)(({ theme }) => ({
  '& .MuiTabs-indicator': {
    backgroundColor: theme.palette.secondary.main,
  },
}));

const StyledTab = styled(Tab)(({ theme }) => ({
  textTransform: 'none',
  fontWeight: theme.typography.fontWeightRegular,
  fontSize: theme.typography.pxToRem(15),
  marginRight: theme.spacing(1),
  '&.Mui-selected': {
    color: theme.palette.secondary.main,
    fontWeight: theme.typography.fontWeightMedium,
  },
  '&.Mui-focusVisible': {
    backgroundColor: theme.palette.action.selected,
  },
}));

function App() {
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState('');
  const [plots, setPlots] = useState({});
  const [tabValue, setTabValue] = useState(0);

  useEffect(() => {
    axios.get('http://localhost:8000/regions')
      .then(response => {
        setRegions(response.data);
        setSelectedRegion(response.data[0]);
      });
  }, []);

  useEffect(() => {
    if (selectedRegion) {
      axios.get(`http://localhost:8000/region/${encodeURIComponent(selectedRegion)}`)
        .then(response => {
          console.log('Received plots:', response.data.plots);
          setPlots(response.data.plots);
        });
    }
  }, [selectedRegion]);

  const handleRegionChange = (event) => {
    setSelectedRegion(event.target.value);
  };

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const tabs = [
    { label: "Average Price", key: "average_price" },
    { label: "Cumulative Change", key: "cumulative_change" },
    ...(selectedRegion !== 'Across the UK' 
      ? [
          { label: "Property Type", key: "property_type" },
          { label: "Property Type Change", key: "property_type_change" }
        ] 
      : []
    )
  ];

  return (
    <ThemeProvider theme={theme}>
      <Container>
        <h1>UK House Price Analysis</h1>
        <RegionSelector
          regions={regions}
          selectedRegion={selectedRegion}
          onRegionChange={handleRegionChange}
        />
        <Box sx={{ width: '100%', mt: 3 }}>
          <AppBar position="static" color="default">
            <StyledTabs
              value={tabValue}
              onChange={handleTabChange}
              variant="scrollable"
              scrollButtons="auto"
            >
              {tabs.map((tab, index) => (
                <StyledTab key={tab.key} label={tab.label} />
              ))}
            </StyledTabs>
          </AppBar>
          {tabs.map((tab, index) => (
            <TabPanel key={tab.key} value={tabValue} index={index}>
              <PlotDisplay plotData={plots[tab.key]} />
            </TabPanel>
          ))}
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;