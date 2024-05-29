mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Initialize counters asd lists
total_missions = 0
success_missions = 0
missions_before_2000 = []

# Process the data using a for loop
for i in range(len(mission_names)):
    # count total number of missions
    total_missions +=1

    # Count number of successful missions
    if mission_success[i]:
        successful_mission +=1

    # Identify and list all missions before 2000
    if mission_years[i] < 2000:
        mission_before_2000.append(mission_names[i])

    # Calculate success rate
    success_rate = (success_missions / total_missions) * 100

    #output the results
    print("total number of missions: {total_missions}")
    print("number of successful missions: {successful_missions}")
    print("success_rate: {success_rate: .2f}%")
    print("missions launced before the year 2000:")
    for mission in missions_before_2000:
        print(f"-{mission}")

         
