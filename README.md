# An open API For BD Covid-19
#### This is a public REST API for accessing district-wise data and daily update for Covid-19 in Bangladesh.

## Documentation

### Home Page:
> GET: https://covidbd-api.herokuapp.com

![home](https://raw.githubusercontent.com/rebornbd/covidbd-api/master/img/home-02.png)

### District data
#### format: json

> GET: https://covidbd-api.herokuapp.com/districts

```
{
    "district": [
        {
            "id": 3,
            "name": "Dhaka",
            "count": 78275
        },
        {
            "id": 4,
            "name": "Dhaka (District)",
            "count": 4527
        },
        {
            "id": 5,
            "name": "Gazipur",
            "count": 4853
        },
        ...............
        ...............
    ],
    "updated_on": "29.08.2020"
}
```

### Division data
#### format: json

> GET: https://covidbd-api.herokuapp.com/divisions

```
{
    "division": [
        {
            "id": 1,
            "name": "Dhaka",
            "total": 119323
        },
        {
            "id": 2,
            "name": "Chattogram",
            "total": 42251
        },
        {
            "id": 3,
            "name": "Sylhet",
            "total": 10558
        },
        ...............
        ...............
    ],
    "updated_on": "29.08.2020"
}
```

### Status data
#### format: json

> GET: https://covidbd-api.herokuapp.com/status

```
{
    "country": "Bangladesh",
    "cases": 310822,
    "todayCases": 1897,
    "deaths": 4248,
    "todayDeaths": 42,
    "recovered": 201907,
    "active": 104667,
    "critical": 0,
    "casesPerOneMillion": 1884,
    "deathsPerOneMillion": 26,
    "totalTests": 1537749,
    "testsPerOneMillion": 9322
}
```

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
============================================================================================
