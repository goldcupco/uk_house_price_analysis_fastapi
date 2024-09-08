import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Tabs,
  Tab,
  Box,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const theme = createTheme();

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

function DataTable({ data }) {
  if (!data || data.length === 0) {
    return <Typography>No data available</Typography>;
  }

  const formatValue = (key, value) => {
    if (key.toLowerCase().includes("date")) {
      return new Date(value).toISOString().split("T")[0];
    } else if (key.toLowerCase().includes("price")) {
      return Number(value).toFixed(2);
    }
    return value;
  };

  return (
    <TableContainer
      component={Paper}
      style={{ maxHeight: 300, overflow: "auto", border: "1px solid #ccc" }}
    >
      <Table stickyHeader aria-label="sticky table">
        <TableHead>
          <TableRow>
            {Object.keys(data[0]).map((key) => (
              <TableCell key={key}>{key}</TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row, index) => (
            <TableRow key={index}>
              {Object.entries(row).map(([key, value], i) => (
                <TableCell key={i}>{formatValue(key, value)}</TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

function App() {
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState("");
  const [plotsData, setPlotsData] = useState({});
  const [tabValue, setTabValue] = useState(0);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/regions")
      .then((response) => {
        setRegions(response.data.regions);
        setSelectedRegion(response.data.regions[0]);
      })
      .catch((error) => console.error("Error fetching regions:", error));
  }, []);

  useEffect(() => {
    if (selectedRegion) {
      axios
        .get(`http://localhost:8000/api/plots/${selectedRegion}`)
        .then((response) => {
          console.log("Received plots:", response.data);
          setPlotsData(response.data);
        })
        .catch((error) => console.error("Error fetching plots:", error));
    }
  }, [selectedRegion]);

  const handleRegionChange = (event) => {
    setSelectedRegion(event.target.value);
    setTabValue(0);
  };

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const formatPlotName = (name) => {
    return name
      .replace(/_/g, " ")
      .split(" ")
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ");
  };

  return (
    <ThemeProvider theme={theme}>
      <Container className="App">
        <Typography variant="h4" component="h1" gutterBottom>
          UK House Price Analysis
        </Typography>
        <FormControl fullWidth margin="normal">
          <InputLabel id="region-select-label">Select Region</InputLabel>
          <Select
            labelId="region-select-label"
            id="region-select"
            value={selectedRegion}
            label="Select Region"
            onChange={handleRegionChange}
          >
            {regions.map((region) => (
              <MenuItem key={region} value={region}>
                {region}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        {plotsData.plots && Object.keys(plotsData.plots).length > 0 && (
          <Box sx={{ width: "100%", mt: 4 }}>
            <Tabs
              value={tabValue}
              onChange={handleTabChange}
              aria-label="plot tabs"
            >
              {Object.keys(plotsData.plots).map((plotName, index) => (
                <Tab
                  label={formatPlotName(plotName)}
                  id={`simple-tab-${index}`}
                  aria-controls={`simple-tabpanel-${index}`}
                  key={plotName}
                />
              ))}
            </Tabs>
            {Object.entries(plotsData.plots).map(
              ([plotName, plotImage], index) => (
                <TabPanel value={tabValue} index={index} key={plotName}>
                  <Typography variant="h6" gutterBottom>
                    {formatPlotName(plotName)}
                  </Typography>

                  <img
                    src={`data:image/png;base64,${plotImage}`}
                    alt={formatPlotName(plotName) || plotName || "Plot image"}
                    style={{ maxWidth: "100%", height: "auto" }}
                  />
                  <img 
  src={`data:image/png;base64,${plotImage}`}
  alt={plotName || "Plot image"}
  style={{ maxWidth: '100%', height: 'auto' }}
/>
                  {plotsData.data && plotsData.data[plotName] && (
                    <DataTable data={plotsData.data[plotName]} />
                  )}
                </TabPanel>
              )
            )}
          </Box>

        )}
      </Container>
    </ThemeProvider>
  );
}

export default App;
