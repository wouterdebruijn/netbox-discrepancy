# Clone latest Netbox from github
git clone -b master https://github.com/netbox-community/netbox.git

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required Python packages
pip install -r netbox/requirements.txt

# Copy the configuration example file
cp configuration.py netbox/netbox/netbox/configuration.py

# Get Python lib folder name
export PYTHON_LIB=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

echo "$(realpath netbox/netbox)" > $PYTHON_LIB/netbox.pth

# Run the database migrations
python3 netbox/netbox/manage.py migrate

# Create a superuser account (interactive)
python3 netbox/netbox/manage.py createsuperuser

echo "🥳 Netbox development environment has been created!"
echo "🚀 To start the development server, run the following command:"
echo "source venv/bin/activate && python3 netbox/netbox/manage.py runserver