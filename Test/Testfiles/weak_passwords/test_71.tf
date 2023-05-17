variable "private_key" {
  description = "The private_key"
  type = string
}

resource "aws_vpc" "nghomzjvjt" {
  private_key = var.private_key
}

output "private_key" {
  value = aws_vpc.nghomzjvjt.private_key
}

module "secure_module" {
  source = "./modules/jfbkjbymxb"
  private_key = var.private_key
}
