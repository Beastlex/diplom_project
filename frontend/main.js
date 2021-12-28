const formUpdate = document.getElementById('update-form');
const formFilter = document.getElementById('filter-form');


const getLastUpdate = () => {
  const updateMsg = document.getElementById('allready-update-msg');
  try {
    const response = await fetch('/last_update');
    const result = await response.json();
    updateMsg.textContent = `${result}`;
  } catch (error) {
    updateMsg.textContent = "There is no update in this year";
  }
  updateMsg.hidden = false;
}; 

formUpdate.addEventListener('submit', (e) => {
  e.preventDefault();
});

formFilter.addEventListener('submit', (e) => {
  e.preventDefault();
});

getLastUpdate();
