variable "location" {
  type    = string
  default = "northeurope"
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
  type        = string
  default     = "~/.ssh/aks-alzver-proj/dbsec.txt"
  description = "Path to file with password for PostgreSQL"
}

variable "dbname" {
  type    = string
  default = "statdb"
}

variable "ssh-public-key" {
  default     = "~/.ssh/aks-alzver-proj/aks-ssh-key.pub"
  description = "SSH Public Key for aks linux nodes"
}
