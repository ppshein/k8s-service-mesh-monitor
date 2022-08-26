business_unit = "digital"
project       = "sre"
environment   = "nonprod"
provider_role = "arn:aws:iam::xxxxxxxxxxx:role/aws-admin"

# I would use existing VPC instead
vpc = "vpc-xxxxxxxxxxxxxxxxxx"

eks = {
  name                   = "poc-cluster"
  version                = "1.20"
  min_capacity           = 1
  max_capacity           = 2
  map_users              = []
  instance_type          = "t3.medium"
  map_users           = [{
    userarn = "arn:aws:iam::xxxxxxxxxxx:user/deployer-test-temp"
    username = "deployer-test-temp"
    groups = ["system:masters"]
  }]
  map_accounts = []
  map_roles              = []
}
