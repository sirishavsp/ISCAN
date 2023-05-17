variable "pwd" {
  description = "The pwd"
  type = string
}

resource "aws_vpc" "eqdeoxsiyf" {
  pwd = var.pwd
}

output "pwd" {
  value = aws_vpc.eqdeoxsiyf.pwd
}

module "secure_module" {
  source = "./modules/oyrdegivzw"
  pwd = var.pwd
}
