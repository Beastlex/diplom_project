terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.91.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg-alzver-proj" {
  name     = "rg-${var.postfix}"
  location = var.location
  tags = {
    owner = var.owner
  }
}

resource "azurerm_log_analytics_workspace" "insights-alzver-proj" {
  name                = "logs-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  retention_in_days   = 30
}
