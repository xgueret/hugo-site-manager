variable "github_token" {
  description = "The GitHub Personal Access Token."
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "The name of the GitHub repository."
  type        = string
  default     = "hugo-site-manager"
}

variable "repository_description" {
  description = "A description for the GitHub repository"
  type        = string
  default     = "Managed by Terraform: This repository automates the process of creating and configuring a new Hugo site. It uses external configuration files to customize site creation and theme setup. "
}

variable "visibility" {
  description = "The visibility of the GitHub repository (public or private)."
  type        = string
  default     = "public"
}