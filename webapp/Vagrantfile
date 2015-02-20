Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.network "private_network", ip: "10.11.12.15"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.synced_folder ".", "/vagrant", type: "nfs"
    config.vm.provision :shell, :inline => "aptitude -q2 update"
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "devops/rolebased.yml"
        ansible.inventory_path = "devops/hosts"
        ansible.limit = 'vagrant'
    config.vm.provision :shell, path: 'bootstrap.sh'
    end
end
