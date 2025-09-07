# ECE2112-PA3
## PROBLEM 1: Using knowledge obtained from the experiment and demonstrations:
a. Load the corresponding .csv file into a data frame named cars using pandas<br>
b. Display the first five and last five rows of the resulting cars


### Step 0: First of all, you need to download the ```cars.csv``` file and save it in the same location as your ```.ipnyb``` notebook before proceeding to the next step.

### Step 1: We need to import the ```pandas```library in order to load and manipulate the ```.csv``` file. We can then use ```pd```as an alias to make referencing shorter when using its functions.
```py
import numpy as np
```

### Step 2: We now use the ```.read_csv()```function to import the data from the ```.csv``` file that we just downloaded and save it to a DataFrame named ```cars```.
```py
cars=pd.read_csv('cars.csv')
```

### Step 2.1: This step is for verification purposes only and not required. We can print out the DataFrame ```cars```to check if the importing was successful.
```py
cars
 Model	                mpg	 cyl disp	  hp	  drat	 wt	qsec vs am gear	carb
0	Mazda RX4	            21.0	6	 160.0	110	  3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	        21.0	6	 160.0	110	  3.90	2.875	17.02	0	1	4	4
2	Datsun 710	          22.8	4	 108.0	93	  3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	      21.4	6	 258.0	110	  3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	    18.7	8	 360.0	175	  3.15	3.440	17.02	0	0	3	2
5	Valiant	              18.1	6	 225.0	105	  2.76	3.460	20.22	1	0	3	1
6	Duster 360	          14.3	8	 360.0	245	  3.21	3.570	15.84	0	0	3	4
7	Merc 240D	            24.4	4	 146.7	62	  3.69	3.190	20.00	1	0	4	2
8	Merc 230	            22.8	4	 140.8	95	  3.92	3.150	22.90	1	0	4	2
9	Merc 280	            19.2	6	 167.6	123	  3.92	3.440	18.30	1	0	4	4
10	Merc 280C	          17.8	6	 167.6	123	  3.92	3.440	18.90	1	0	4	4
11	Merc 450SE	        16.4	8	 275.8	180	  3.07	4.070	17.40	0	0	3	3
12	Merc 450SL	        17.3	8	 275.8	180	  3.07	3.730	17.60	0	0	3	3
13	Merc 450SLC	        15.2	8	 275.8	180	  3.07	3.780	18.00	0	0	3	3
14	Cadillac Fleetwood	10.4	8	 472.0	205	  2.93	5.250	17.98	0	0	3	4
15	Lincoln Continental	10.4	8	 460.0	215	  3.00	5.424	17.82	0	0	3	4
16	Chrysler Imperial	  14.7	8	 440.0	230	  3.23	5.345	17.42	0	0	3	4
17	Fiat 128	          32.4	4	 78.7	  66	  4.08	2.200	19.47	1	1	4	1
18	Honda Civic	        30.4	4	 75.7	  52	  4.93	1.615	18.52	1	1	4	2
19	Toyota Corolla	    33.9	4	 71.1	  65	  4.22	1.835	19.90	1	1	4	1
20	Toyota Corona	      21.5	4	 120.1	97	  3.70	2.465	20.01	1	0	3	1
21	Dodge Challenger	  15.5	8	 318.0	150	  2.76	3.520	16.87	0	0	3	2
22	AMC Javelin	        15.2	8	 304.0	150	  3.15	3.435	17.30	0	0	3	2
23	Camaro Z28	        13.3	8	 350.0	245	  3.73	3.840	15.41	0	0	3	4
24	Pontiac Firebird	  19.2	8	 400.0	175	  3.08	3.845	17.05	0	0	3	2
25	Fiat X1-9	          27.3	4	 79.0	  66	  4.08	1.935	18.90	1	1	4	1
26	Porsche 914-2	      26.0	4	 120.3	91	  4.43	2.140	16.70	0	1	5	2
27	Lotus Europa	      30.4	4	 95.1	  113	  3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	    15.8	8	 351.0	264	  4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	      19.7	6	 145.0	175	  3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	      15.0	8	 301.0	335	  3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	        21.4	4	 121.0	109	  4.11	2.780	18.60	1	1	4	2

```


### Step 3: We can now return the first 5 rows of the said DataFrame by using the ```.head()``` method. Similarly, we can also return the last 5 rows by using the ```.tail()``` method. After this, we need to combine both sets of rows into a single table. To do this, we place them inside a Python list and pass it to the ```pd.concat()``` function, like so:
```py
pd.concat([cars.head(), cars.tail()])
Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	21.0	6	160.0	110	3.90	2.875	17.02	0	1	4	4
2	Datsun 710	22.8	4	108.0	93	3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	21.4	6	258.0	110	3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	18.7	8	360.0	175	3.15	3.440	17.02	0	0	3	2
27	Lotus Europa	30.4	4	95.1	113	3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	15.8	8	351.0	264	4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	19.7	6	145.0	175	3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	15.0	8	301.0	335	3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2
```
<br>

## PROBLEM 2: Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.<br>
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.<br>
c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?<br>
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. <br> 

### Step 0: Similarly, to the first problem, we need to have the ```cars.csv``` file downloaded and save to the same location as out ```.ipnyb```notebook before we can proceed.

### Step 1: Again, we need to import the ```pandas```library as this contains all the functions and methods that we will be using later. Also, we import it as ```pd``` so that the referencing will be shorter when using it.
```py
import pandas as pd
```

### Step 2: We can now then use the ```.read_csv()``` function to load the ```.csv``` file into a DataFrame named ```cars```.
```py
cars=pd.read_csv('cars.csv')
```

### Step 2.1: For verification purposes, we can print out the DataFrame to check if it was successful.
```py
cars

  Model	                mpg	 cyl disp	  hp	  drat	 wt	qsec vs am gear	carb
0	Mazda RX4	            21.0	6	 160.0	110	  3.90	2.620	16.46	0	1	4	4
1	Mazda RX4 Wag	        21.0	6	 160.0	110	  3.90	2.875	17.02	0	1	4	4
2	Datsun 710	          22.8	4	 108.0	93	  3.85	2.320	18.61	1	1	4	1
3	Hornet 4 Drive	      21.4	6	 258.0	110	  3.08	3.215	19.44	1	0	3	1
4	Hornet Sportabout	    18.7	8	 360.0	175	  3.15	3.440	17.02	0	0	3	2
5	Valiant	              18.1	6	 225.0	105	  2.76	3.460	20.22	1	0	3	1
6	Duster 360	          14.3	8	 360.0	245	  3.21	3.570	15.84	0	0	3	4
7	Merc 240D	            24.4	4	 146.7	62	  3.69	3.190	20.00	1	0	4	2
8	Merc 230	            22.8	4	 140.8	95	  3.92	3.150	22.90	1	0	4	2
9	Merc 280	            19.2	6	 167.6	123	  3.92	3.440	18.30	1	0	4	4
10	Merc 280C	          17.8	6	 167.6	123	  3.92	3.440	18.90	1	0	4	4
11	Merc 450SE	        16.4	8	 275.8	180	  3.07	4.070	17.40	0	0	3	3
12	Merc 450SL	        17.3	8	 275.8	180	  3.07	3.730	17.60	0	0	3	3
13	Merc 450SLC	        15.2	8	 275.8	180	  3.07	3.780	18.00	0	0	3	3
14	Cadillac Fleetwood	10.4	8	 472.0	205	  2.93	5.250	17.98	0	0	3	4
15	Lincoln Continental	10.4	8	 460.0	215	  3.00	5.424	17.82	0	0	3	4
16	Chrysler Imperial	  14.7	8	 440.0	230	  3.23	5.345	17.42	0	0	3	4
17	Fiat 128	          32.4	4	 78.7	  66	  4.08	2.200	19.47	1	1	4	1
18	Honda Civic	        30.4	4	 75.7	  52	  4.93	1.615	18.52	1	1	4	2
19	Toyota Corolla	    33.9	4	 71.1	  65	  4.22	1.835	19.90	1	1	4	1
20	Toyota Corona	      21.5	4	 120.1	97	  3.70	2.465	20.01	1	0	3	1
21	Dodge Challenger	  15.5	8	 318.0	150	  2.76	3.520	16.87	0	0	3	2
22	AMC Javelin	        15.2	8	 304.0	150	  3.15	3.435	17.30	0	0	3	2
23	Camaro Z28	        13.3	8	 350.0	245	  3.73	3.840	15.41	0	0	3	4
24	Pontiac Firebird	  19.2	8	 400.0	175	  3.08	3.845	17.05	0	0	3	2
25	Fiat X1-9	          27.3	4	 79.0	  66	  4.08	1.935	18.90	1	1	4	1
26	Porsche 914-2	      26.0	4	 120.3	91	  4.43	2.140	16.70	0	1	5	2
27	Lotus Europa	      30.4	4	 95.1	  113	  3.77	1.513	16.90	1	1	5	2
28	Ford Pantera L	    15.8	8	 351.0	264	  4.22	3.170	14.50	0	1	5	4
29	Ferrari Dino	      19.7	6	 145.0	175	  3.62	2.770	15.50	0	1	5	6
30	Maserati Bora	      15.0	8	 301.0	335	  3.54	3.570	14.60	0	1	5	8
31	Volvo 142E	        21.4	4	 121.0	109	  4.11	2.780	18.60	1	1	4	2

```

### Step 3: For item A, we can use the ```.iloc()``` method to subset the DataFrame. ```:5```selects the first 5 rows (indices 0 to 4), while ```::2```selects every other column, starting from the first one.
```py
cars.iloc[:5, ::2]

  Model	            cyl	hp	  wt	  vs	gear
0	Mazda RX4	        6	  110	  2.620	  0	  4
1	Mazda RX4 Wag	    6	  110	  2.875	  0	  4
2	Datsun 710	      4	  93	  2.320	  1	  4
3	Hornet 4 Drive	  6	  110	  3.215	  1	  3
4	Hornet Sportabout	8	  175	  3.440	  0	  3
```

### Step 4: For item B, we need to locate and display the row where the ```Model``` column matches "Mazda RX4".
```py
cars[cars["Model"] == "Mazda RX4"]

  Model	    mpg	  cyl	  disp	  hp	  drat	  wt	  qsec	  vs	  am	  gear	  carb
0	Mazda RX4	21.0	6	    160.0	  110	  3.9	    2.62	16.46	   0	   1	   4	      4
```

### Step 5: For item C, we first need to locate the row where the ```Model``` column matches "Camaro Z28", and from that row, we need to display its corresponding ```cyl```value.
```py
cars.loc[cars["Model"] == "Camaro Z28", ["Model", "cyl"]]

    Model	     cyl
23	Camaro Z28	8
```

### Step 6: For item D, we first need to locate and display the rows where the ```Model``` column matches "Mazda RX4 Wag", "Ford Pantera L" and "Honda Civic". From that, we also need to display only their corresponding ```cyl``` value and ```gear``` type.
```py
cars.loc[[1, 28, 18], ['Model','cyl','gear']]

    Model	          cyl	gear
1	  Mazda RX4 Wag	   6    4
28	Ford Pantera L 	 8	  5
18	Honda Civic	     4	  4
```
