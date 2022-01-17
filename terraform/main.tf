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
