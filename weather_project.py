#application to get the weather via openweathermap.org using city or zip code

import requests   # reuqest module

def welcome():    # function for welcome message
	print('Welcome to your weather application')

def get_city(): # function to get weather by city
 	city = input('Enter a city : ') # user input
 	if city.isdigit(): # chaking if user input was a number
 		print ('Your city contains a number try again') 
 	else:
 		city_url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=imperial&appid=904bd70c6fe9d536e7be0840a7ee0357' # url from website to request weather by city
 		weather_data = requests.get(city_url).json() # passign json to weather data
 		try:
 			response = requests.get(city_url) # getting a response from the website
 			if (response.status_code == 200): # cheking if the response from the website is good 200 = ok  
 				print ('\nconnection successful\n')
 				print('\nThe current weather data for the city of ' + city +':\n')
 				weatherDict=weather_data # passing the weather data to a dictionary 
 		
 				latitude = weatherDict['coord']['lat']
 				longitude = weatherDict['coord']['lon']
 				feelsLike = weatherDict['main']['feels_like']          # here we pass the values from  
 				description = weatherDict['weather'][0]['description'] # the dictionary to variables
 				temp = weatherDict['main']['temp']                     # to make the formating of  
 				highTemp = weatherDict['main']['temp_max']             # the output easier to read
 				lowTemp = weatherDict['main']['temp_min']
 				windSpeed = weatherDict['wind']['speed']
 				pressure = weatherDict['main']['pressure']
 				humidity = weatherDict['main']['humidity']
 				# output of weather information
 				print('Latitude : {}'.format(latitude) + ' Longitude : {}'.format(longitude))
 				print('Feels like : {} °F'.format(feelsLike) + ' and the description is : {}'.format(description))
 				print('The Current Temperature : {} °F'.format(temp) +' wiht a Low of: {} °F'.format(lowTemp) + ' and a High : {} °F'.format(highTemp))
 				print('Wind Speed is : {} m/s'.format(windSpeed))
 				print('Pressure : {} hPa'.format(pressure))
 				print('Humidity : {} %'.format(humidity))
 			else:
 				print('No data found try again') # message if the website response was bad
 		except:
 			print('connection was unsuccessful')
 	
 			

def get_zip(): # function to get weather by zip code
	zip_code = input('Enter a zip code : ')
	while len(zip_code) != 5: # cheking if user input is not 5 digits
		print ('Please enter a 5 digit zip code')
		zip_code = input('Enter a zip code : ')
		if len(zip_code) == 5: # if user input of 5 digits is ok 
			zip_url = 'http://api.openweathermap.org/data/2.5/weather?zip='+ zip_code + '&units=imperial&appid=904bd70c6fe9d536e7be0840a7ee0357' # url from website to request weather by zip code
			weather_data = requests.get(zip_url).json() # passign json to weather data
			try:
				response = requests.get(zip_url)# getting a response from the website
				if (response.status_code == 200): # cheking if the response from the website is good 200 = ok 
					print ('\nconnection successful\n')
					print('\nThe current weather information for the zip code ' + zip_code +':\n')
					weatherDict=weather_data # passing the weather data to a dictionary 
	
					latitude = weatherDict['coord']['lat']
					longitude = weatherDict['coord']['lon']
					feelsLike = weatherDict['main']['feels_like']          # here we pass the values from 
					description = weatherDict['weather'][0]['description'] # the dictionary to variables
					temp = weatherDict['main']['temp']                     # to make the formating of  
					highTemp = weatherDict['main']['temp_max']             # the out put easier to read
					lowTemp = weatherDict['main']['temp_min']
					windSpeed = weatherDict['wind']['speed']
					pressure = weatherDict['main']['pressure']
					humidity = weatherDict['main']['humidity']
					# output of weather information
					print('Latitude : {}'.format(latitude) + ' Longitude : {}'.format(longitude))
					print('Feels like : {} °F'.format(feelsLike) + ' and the description is : {}'.format(description))
					print('The Current Temperature : {} °F'.format(temp) +' wiht a Low of: {} °F'.format(lowTemp) + ' and a High : {} °F'.format(highTemp))
					print('Wind Speed is : {} m/s'.format(windSpeed))
					print('Pressure : {} hPa'.format(pressure))
					print('Humidity : {} %'.format(humidity))
				else:
					print('No data found try again') # message if the website response was bad
			except:
				print('connection was unsuccessful')

def main(): # main function
	again = str('go') # value to initialize the loop
	welcome()
	while again != str('q'): # loop
		again= input('\nPlease enter city to search by city, zip code to search by zip code or q to exit:\n') # user input
		if again == ('city'): # if user selects city we use the city function
			get_city()
		elif again == ('zip code'): # if user selects zip code we use the zip code function
			get_zip()
		elif again == str('q'): # value to exit the program
			print ('Good Bye') # good bye message	
		else:
			print('Please select a valid entry city, zip code or q to exit. ')

if __name__ =='__main__':
	main()
