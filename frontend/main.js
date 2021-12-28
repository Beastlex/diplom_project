const formUpdate = document.getElementById('update-form');
const formFilter = document.getElementById('filter-form');


const getLastUpdate = async () => {
  const updateMsg = document.getElementById('allready-update-msg');
  try {
    const response = await fetch('/api/last_update');
    const result = await response.json();
    updateMsg.textContent = `${result}`;
  } catch (error) {
    updateMsg.textContent = "There is no update in this year";
  }
  updateMsg.hidden = false;
}; 

const getCountryList = async () => {
  const counrtyList = document.getElementById('country-sel');
  try {
    const response = await fetch('/api/countries');
    const result = await response.json();
    for (country of result.sort()) {
      let newOption = document.createElement('option');
      newOption.value = country
      newOption.text = country
      counrtyList.add(newOption, null)
    }
  } catch (error) {
    console.log("Could not load country list. Is it updated?");
  }
};

const performUpdate = async () => {
  try {
    const response = await fetch('/api/update');
    if (response.status == '200') {
      getLastUpdate();
    } else {
      console.log("Update in progress " + response.status);
    }
  } catch (error) {
    console.log("Update error!")
  }
};

const fillTable = (data) => {
  const tableBody = document.querySelector('tbody');
  const tableData = data.map((item) => {
    return `
    <tr>
    <td>${item.date_value}</td>
    <td>${item.country_code}</td>
    <td>${item.confirmed}</td>
    <td>${item.deaths}</td>
    <td>${item.stringency_actual}</td>
    <td>${item.stringency}</td>
    </tr>
    `;
  }).join('');
  tableBody.innerHTML = tableData;
}

const getStatistics = async () => {
  const countryList = document.getElementById('country-sel');
  const orderList = document.getElementById('sort-order-sel');

  countryText = countryList.options[countryList.selectedIndex].value;
  orderText = orderList.options[orderList.selectedIndex].value;

  const uriQuery = `/api/stats/${countryText}/${orderText}`;
  try {
    const response = await fetch(uriQuery);
    const data = await response.json();
    fillTable(data.statistics);
  } catch (error) {
    console.log("Could not load statics");
    console.log(error);
  }
};

formUpdate.addEventListener('submit', (e) => {
  e.preventDefault();
  performUpdate();
});

formFilter.addEventListener('submit', (e) => {
  e.preventDefault();
  getStatistics();
});

getLastUpdate();
getCountryList();
