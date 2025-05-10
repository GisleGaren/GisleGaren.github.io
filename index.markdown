---

layout: page
permalink: /
styles:
  - /assets/css/custom.css

---

<style>
body {
    background-color:rgb(255, 255, 255);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.page-content {
    background-image: url('./images/background.jpg');  /* Update this path */
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;  
    padding: 20px;
    border-radius: 10px;
    min-height: 100vh;  /* ensures it always fills the viewport */
}

a:hover {
  color: #007acc;
  text-decoration: underline;
  font-weight: bold;
}

.image-block p {
  font-size: 1.1rem;
  color: #3d1f23;
  font-family: 'Georgia', serif;
  line-height: 1.6;
  margin-top: 15px;
  background-color: #fff8f4;
  padding: 15px 20px;
  border-left: 4px solid #e07a5f;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}


.comments {
  font-size: 1.1rem;
  color: #3d1f23;
  font-family: 'Georgia', serif;
  line-height: 1.6;
  margin-top: 15px;
  background-color: #fff8f4;
  padding: 15px 20px;
  border-left: 4px solid #e07a5f;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

</style>

<div style="display: flex; justify-content:center; border-radius: 10px; margin-bottom: 20px; gap: -10vw;" >
  <div>
    <h1 style="font-weight: bold; font-size: 2.5rem; width: 23vw; font-style: italic;">This, is Javi and he needs your help!</h1>
  </div>
  <div>
    <!-- Replace the src with your actual GIF URL -->
    <img src="./images/fingerPointingDown.gif" alt="Javi in action" style="width: 8vh;">
  </div>
</div>

<div style="display: flex; justify-content: center; margin-top: 3vh; margin-bottom: 14vh">
  <img src="./images/javi.jpeg" alt="Javi photo" style="width: 50vh; border-radius: 10vh;">
</div>

<div style="margin-top: 10vh; margin-bottom: 2vh; max-width: 600px;">
  <h2 style="margin-top: 0; font-weight: bold; font-size: 2rem;">📚 Table of Contents</h2>
  <ul style="list-style-type: none; padding-left: 0.5rem; font-size: 1.2rem; line-height: 2;">
    <li style="margin-bottom: 8px;">
      <a href="#intro-javi" style="color: black;">
        <strong>1. 👋</strong> Introduction: Meet Javi
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#dangerous-hours" style="color: black;">
        <strong>2. 🕒</strong> Dangerous Hours
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#dangerous-places" style="color: black;">
        <strong>3. 📍</strong> Dangerous Places
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#vehicle-info" style="color: black;">
        <strong>4. 🚗</strong> Vehicles Involved and Causes of Crash
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#who-gets-hurt" style="color: black;">
        <strong>5. 🤕</strong> Who Gets Hurt?
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#bike-danger" style="color: black;">
        <strong>6. ⚠️</strong> Where should Javi be careful on his bike?
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#conclusion" style="color: black;">
        <strong>7. ✅</strong> Conclusion: What should Javi do?
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#references" style="color: black;">
        <strong>8. 🔗</strong> References
      </a>
    </li>
  </ul>
</div>

<div id="intro-javi" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">
    1. Introduction: Meet Javi
  </h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">
    We at Sune Analytics found this on the frontpage of this newspaper and we sympathize with his story. 
    We decided to take matters into our own hands by analyzing traffic data in New York City to help deliver people like Javi navigate through its busy streets!
  </p>
</div>

<img src="/images/newspaper.png" alt="Newspaper with Javi delivery guy" style="width: 35vw; display: block; margin: auto; border-radius: 10px;" />

<div id="dangerous-hours" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">2. Dangerous Hours</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">
    The interactive bar chart visualizes the frequency of vehicle collisions involving Uber drivers in New York City, broken down by hour of the day and day of the week.
    Each hour from midnight (00:00) to 11 PM (23:00) is shown along the x-axis, and the y-axis represents the total number of recorded collisions.
    The bars are grouped and color-coded by day of the week, helping highlight temporal patterns in collision risk.
  </p>
</div>

<iframe 
  src="{{ '/assets/dangerous_hours_plot.html' | relative_url }}" 
  width="1200" 
  height="600"
  frameborder="0"
  scrolling="no"
></iframe>

<div class="comments" style="margin-top: 5vh;">
  <p>
    Collision peaks tend to occur during rush hours (7–9 AM and 4–7 PM), especially on weekdays.
    Fridays often show higher evening collisions, likely due to increased ride demand and traffic congestion.
    On weekends, while overall collisions are lower, some late-night risk persists due to nightlife activity (1–3 AM).
  </p>
</div>

<div id="dangerous-places" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">3. Dangerous Places</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Interactive Map of Collision Locations like the one we had in assignment 2.</p>
</div>

# Add your plot here

<div id="vehicle-info" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">4. Vehicles Involved and Causes of Crash</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">When traversing through the city, what are the main vehicles involved in the collisions and what were the main factors that caused them?</p>
</div>

<img src="/images/pieChartVehicleShare.png" alt="Top Vehicle Types in Collisions" style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />

<div class="comments" style="margin-bottom:5vh">
  <p>From the pie chart, we can observe that most vehicles registered as collision data are motor vehicles - primarily SUVs and sedans. For Javi on his bike, this constitutes a relatively small proportion of registered collisions. The keyword here is registered, as a significant proportion of bicycle accidents go unreported to the police[1].</p>
  <p>According to the American Community Survey from 2017 - 2021, bicycles constituted 1.4% of the commute, whilst cars, trucks or vans constituted 26.8% of the commute[2]. With only SUVs and Sedans themselves cumulatively being 75% of all accidents in our pie chart, means that they are grossly over represented in terms of their proportion of crashes.</p>
  <p>Javi explicitly mentions that he is considering other forms of transportation. What does he especially need to take into consideration when operating other vehicle types?</p>
</div>

<h3 style="font-size: 2.2rem; font-family: 'Georgia', serif; text-align: center;">Cause Of Crash For Each Vehicle</h3>
<!-- SUV -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/suvContributingFactors.png" 
       alt="SUV Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p>A common theme of driver inattention and distractions seem to be standard amongst all modes of transport. This makes sense as being on the phone or maybe adjusting the radio for even a split second can mean the difference between life or death. Being patient by yielding when in douby and keep distance from other vehicles when driving is key with avoiding accidents in SUVs.</p>
</div>

<!-- Sedan -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/sedanContributingFactors.png" 
       alt="Sedan Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p style="text-align:center;">Very similiar to the SUV factors as both vehicles operate in a similiar manner.</p>
</div>

<!-- Bicycle -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/bikeContributingFactors.png" 
       alt="Bicycle Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p>Failing to yield on a bike and pedestrian errors often go hand in hand as uncertainty around yielding leads to incidents with pedestrians. For Javi, giving proper signals, being predictable and yielding when in doubt should especially be highlighted.</p>
</div>

<!-- Motorcycle -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/motorbikeContributingFactors.png" 
       alt="Motorcycle Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
      <p>If on a motorcycle, be especially careful with lane usage as well as speeds.</p>
</div>

<!-- Van -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/vanContributingFactors.png" 
       alt="Van Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
  <p>Backing unsafely in a van makes sense as vans often have large blindspots and are filled with cargo making it difficult to see from behind. Drowsyness and fatigue was an interesting one, perhaps indicating that van drivers usually drive for long distances transporting goods, thereby contributing to fatigue?</p>
</div>

<div id="who-gets-hurt" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">5. Who Gets Hurt?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Charts to explore injury demographics by age, sex, and transport mode (pedestrian, cyclist, etc).</p>
</div>

# Add your plot here

<div id="bike-danger" style="
  margin-top: 7vh;
  margin-bottom: 5vh;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">6. Where Should Javi Be Careful On His Bike?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Javi, like many others delivers food on his bike, it's good exercise, good for the environment and it's relatively affordable in maintenance costs. Where in the city should he especially be careful when riding his bike?</p>
</div>

<h3 style="font-size: 1rem; font-family: 'Georgia', serif; text-align: center;">Below is an interactive map showing places in New York with cyclist injuries of at least 2 or a death. There is also a toggle for a heatmap to see a smoother transition in concentration for bicycle incidents. </h3>

<iframe
  src="{{ '/assets/cyclist_map.html' | relative_url }}" 
  width="1000px"
  height="600px"
  style="border:none;"
  loading="lazy"
></iframe>

<div class="comments">
  <p>Our map portrays injuries as orange markers and deaths as red markers, where bigger markers indicate more incidences of either injuries or deaths. Click on each marker in order to see more information about the incident like time. The heatmap includes all bicycle incidents to supplement any findings and based on this information, we can see concentrations of incidents in Manhatten, especially around the bowery regions and the path north leading to Midtown. Javi should exercise more caution around these areas. By utilizing this map, Javi can plan routes more effectively. What other routes would you avoid if you were Javi?</p>
</div>

<div id="conclusion" style="
  margin: 8vh auto 5vh auto;
  max-width: 800px;
  background: linear-gradient(135deg, #fef6e4 0%, #fcd5ce 100%);
  padding: 40px 30px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  border: 1px solid #e0b1a0;
  font-family: 'Georgia', serif;
">
  <h2 style="
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: #49111c;
    font-family: 'Playfair Display', Georgia, serif;
    letter-spacing: 0.5px;
  ">7. Conclusion: What should Javi do?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Summarize patterns to offer takeaways like avoiding certain hours or locations.</p>
</div>

### References

[1] Geus, B. de, et al. “Under-Reporting Bicycle Accidents to Police in the Cost TU1101 International Survey: Cross-Country Comparisons and Associated Factors.” Accident Analysis & Prevention, Pergamon, 26 Oct. 2017, www.sciencedirect.com/science/article/pii/S0001457517303391. 

[2] American Community Survey. “Walking, Driving, and Cycling Data for NYC.” Environment & Health Data Portal, 2021, a816-dohbesp.nyc.gov/IndicatorPublic/data-explorer/walking-driving-and-cycling/?id=2415#display=summary. 
