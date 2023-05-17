variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_db_instance" "amuxwxfgcm" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_db_instance.amuxwxfgcm.pwd
}

module "secure_module" {
  source = "./modules/dtronlxcvl"
  pwd = var.pwd
}
