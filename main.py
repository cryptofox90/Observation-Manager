from visualization import show_graph
import sqlite3
import csv
from observation import Observation
import numpy as np
from database import save_observations_to_db

observations =[]

def add_observation():
    target = input("Target: ")
    try: 
        exposure = float(input("Exposure time(Second)"))
    except ValueError:
        print("Exposure time should be a int or float")
        return 
    observer = input("Name of observer")
    filt = input("Filter name: ")
    obs = Observation(target, observer, filt, exposure)
    observations.append(obs)
    print("Observation added Succesfully")
def show_observation():
    if len(observations) == 0:
        print("No Observation found")
        return
    else:
        for i, obs in enumerate(observations):
            print(f" Observation >>> {i + 1}\n Target: {obs.target}")
            print(f" exposure: {obs.exposure}")
            print(f" observer : {obs.observer}")
            print(f" filter: {obs.filter}")
def search_observation():
    user = input("Target: ")
    found = False
    for obs in observations:
        if user.lower() == obs.target.lower():
            print("Observation found\n")
            print(f"Target: {obs.target}")
            print(f"Exposure: {obs.exposure}")
            print(f"Observer: {obs.observer}")
            print(f"Filter: {obs.filter}")
            found = True
    if not found:
        print("No target name found")
    
def average_exposure():
    exposures = []
    for obs in observations:
        exposures.append(obs.exposure)
    exposures = np.array(exposures)
    aver = np.average(exposures)
    print(f"average exposure time is {aver} sec")
def max_exposure():
    exposures = []
    for obs in observations:
        exposures.append(obs.exposure)
    exposures = np.array(exposures)
    maxe = np.max(exposures)
    print(f"Max exposure time is {maxe} sec")
def min_exposure():
    exposures = []
    for obs in observations:
        exposures.append(obs.exposure)
    exposures = np.array(exposures)
    mine = np.min(exposures)
    print( f"Min exposure time is {mine} sec")
def total_exposure():
    exposures = []
    for obs in observations:
        exposures.append(obs.exposure)
    exposures = np.array(exposures)
    total = np.sum(exposures)
    print( f"Sum of exposure time is {total} sec")
def save_to_file():
    filename = input("Your file name")
    with open(f"{filename}.csv", "w", newline="") as csvfile:
        fieldnames = [
            "target",
            "observer",
            "exposure(S)",
            "filter"
            ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obs in observations:
            row = {
                "target": obs.target,
                "observer":obs.observer,
                "exposure(S)":obs.exposure,
                "filter":obs.filter
                
            }
            writer.writerow(row)
conn = sqlite3.connect("observation.db")
    
while True:
    print("=" * 40)
    print()
    print("Welcome to Observer Log".center(40))
    print()
    print("=" * 40)
    print("1. Add Observation")
    print("2. Show Observation")
    print("3. Average exposure")
    print("4. Maximum exposure")
    print("5. Minimum Exposure")
    print("6. Total exposure")
    print("7. Search observation")
    print("8. Save to file")
    print("9. Show graph")
    print("10.Save to database")
    print("0. Exit")
    choice = input("Choose:")
    if choice == "1":
        add_observation()
    elif choice == "2":
        show_observation()
    elif choice == "3":
        average_exposure()
    elif choice == "4":
        max_exposure()
    elif choice == "5":
        min_exposure()
    elif choice == "6":
        total_exposure()
    elif choice == "7":
        search_observation()
    elif choice == "8":
        save_to_file()
    elif choice == "9":
        show_graph(observation)
    elif choice == "10":
        save_observations_to_db(observations, conn)        
    elif choice == "0":
        break
    else: 
        print("Please select 1 to 9")        
conn.close()     
    