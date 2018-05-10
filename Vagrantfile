Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.provider :aws do |aws, override|
    aws.access_key_id = ENV['AWS_ACCESS_KEY']
    aws.secret_access_key = ENV['AWS_SECRET_KEY']
    aws.keypair_name = ENV['AWS_EC2_KEY_NAME']
    aws.region = ENV['AWS_DEFAULT_REGION']
    aws.security_groups = "default"
    aws.instance_type="t2.micro"
    aws.elastic_ip="34.253.52.245"


    aws.ami = "ami-f90a4880"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = ENV['AWS_PRIVATE_KEY_PATH']
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "Playbook.yml"
  end


end
