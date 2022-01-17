resource "azurerm_virtual_network" "vnet-alzver-proj" {
  name = "vnet-${var.postfix}"
  location  = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  address_space = ["10.0.0.0/16"]
  tags = {
    owner = var.owner
  }
}

resource "azurerm_subnet" "subnet-gw" {
  name = "subnet-gw"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  virtual_network_name = azurerm_virtual_network.vne-alzver-proj
  address_prefix = "10.0.1.0/24"
}

resource "azurerm_subnet" "subnet-db" {
  name = "subnet-db"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  virtual_network_name = azurerm_virtual_network.vne-alzver-proj
  address_prefix = "10.0.2.0/24"
}

resource "azurerm_subnet" "subnet-aks" {
  name = "subnet-aks"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  virtual_network_name = azurerm_virtual_network.vne-alzver-proj
  address_prefix = "10.0.3.0/24"
}
