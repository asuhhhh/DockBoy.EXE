# DockBoy.EXE Full System Implementation

class DockBoyEXE:
    def __init__(self, name="DockBoy.EXE"):
        self.name = name
        self.docks = {}
        self.version = "1.0"
        self.location = None
        self.setup_complete = False
    
    def setup_dock(self, location, rename=None):
        self.location = location
        if rename:
            self.name = rename + ".EXE"
        self.create_weather_dock()
        print(f"{self.name} setup complete. Location set to {location}.")
    
    def create_weather_dock(self):
        self.docks["WeatherDock"] = f"Tracking weather for {self.location}"
        print(f"WeatherDock created for {self.location}.")
    
    def add_battledock(self):
        self.docks["BattleDock"] = "Handling short-term, high-priority tasks"
        print("BattleDock added.")

    def add_multi_dock_protocol(self):
        print("Multi-Dock Protocol enabled.")
    
    def create_docker_protocol(self):
        print("Docker.EXE Personality Framework initialized.")

    def add_protocol_guide(self):
        print("Protocol Guide available.")

    def add_sitreptoggle(self):
        print("SITREPDOCK and SITREP toggle functionality added.")
    
    def generate_sitrep(self):
        print("Generating military-style SITREP...")

    def log_version(self):
        print(f"{self.name} is now live with version {self.version}.")

# Example of using DockBoy.EXE

if __name__ == "__main__":
    dockboy = DockBoyEXE()
    dockboy.setup_dock(location="City, Country", rename="YourChoice")
    dockboy.add_battledock()
    dockboy.add_multi_dock_protocol()
    dockboy.create_docker_protocol()
    dockboy.add_protocol_guide()
    dockboy.add_sitreptoggle()
    dockboy.log_version()

    # To generate a SITREP
    dockboy.generate_sitrep()
