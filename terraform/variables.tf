variable "location" {
  type    = string
  default = "northurope"
}

variable "postfix" {
  type    = string
  default = "alzver-proj"
}

variable "owner" {
  type    = string
  default = "Aleksandr_Zverev1@epam.com"
}

variable "pglogin" {
  type    = string
  default = "psqladmin"
}

variable "pgpasswd" {
  type    = string
  default = "Type password in terraform.tfvars"
}

variable "dbname" {
  type    = string
  default = "statdb"
}

variable "ssh-public-key" {
  default     = "~/.ssh/aks-alzver-proj/aks-ssh-key.pub"
  description = "SSH Public Key for aks linux nodes"
}
