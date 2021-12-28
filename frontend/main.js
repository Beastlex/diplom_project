const formUpdate = document.getElementById('update-form');
const formFilter = document.getElementById('filter-form');


const getLastUpdate = () => {
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

const getCountryList = () => {
  const counrtyList = document.getElementById('country-sel');
  try {
    const response = await fetch('/api/counties');
    const result = await response.json();
    for (country in result) {
      let newOption = new Option(country, country);
      counrtyList.append(newOption);
    }
  } catch (error) {
    console.log("Could not load country list. Is it updated?");
  }
};

const performUpdate = () => {
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

formUpdate.addEventListener('submit', (e) => {
  e.preventDefault();
  performUpdate();
});

formFilter.addEventListener('submit', (e) => {
  e.preventDefault();
});

getLastUpdate();
getCountryList();
