variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_vpc" "bohdtisivb" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_vpc.bohdtisivb.private_key
}

module "secure_module" {
  source = "./modules/unmkiebzve"
  private_key = var.private_key
}
