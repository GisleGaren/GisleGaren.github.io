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
        <strong>4. 🚗</strong> What share of vehicles are involved in the crashes?
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

<div style="margin-top: 5vh;">
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

<img src="/images/pieChartVehicleShare.png" alt="Top Vehicle Types in Collisions" style="width: 35vw; display: block; margin: auto; border-radius: 10px;" />

<div>
  <p>From the pie chart, we can observe that most vehicles registered as collision data are motor vehicles - primarily SUVs and sedans. For Javi on his bike, this constitutes a relatively small proportion of registered collisions. The keyword here is registered, as a significant proportion of bicycle accidents go unreported to the police[1].</p>
  <p>According to the American Community Survey from 2017 - 2021, bicycles constituted 1.4% of the commute, whilst cars, trucks or vans constituted 26.8% of the commute [2]. With only SUVs and Sedans themselves cumulatively being 75% of all accidents in our pie chart, means that they are grossly over represented in terms of their proportion of crashes.</p>
  <p>Javi explicitly mentions that he is considering other forms of transportation. What does he especially need to take into consideration when operating other vehicle types?</p>
</div>

<h3>Biggest contributions to collisions based on vehicle</h3>
<!-- SUV -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/suvContributingFactors.png" 
       alt="SUV Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p>A common theme of driver inattention and distractions seem to be standard amongst all modes of transport. Being patient by yielding when in douby and keep distance from other vehicles when driving is key with avoiding accidents in SUVs.</p>
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
  ">6. Where should Javi be careful on his bike?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Ayy Lmao</p>
</div>

<iframe
  src="{{ '/assets/cyclist_map.html' | relative_url }}" 
  width="1000px"
  height="600px"
  style="border:none;"
  loading="lazy"
></iframe>


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
  ">7. Conclusion: Can Javi Make It?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Summarize patterns to offer takeaways like avoiding certain hours or locations.</p>
</div>

<!--
<div style="background-color:#f0f8ff; padding:20px; border-radius:10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2 style="font-weight:bold;">⚠️ A Day in the Life of Javi</h2>
  <p>
    New York City is the city that never sleeps and no address within New York City is beyond Javi's reach!
    Delivering food in its busy streets is dangerous, so how can we help Javi deliver food as safely as possible?
  </p>
</div>
-->

### References

[1] https://www.sciencedirect.com/science/article/pii/S0001457517303391

[2] https://a816-dohbesp.nyc.gov/IndicatorPublic/data-explorer/walking-driving-and-cycling/?id=2415#display=summary

[3] Sheppard, H. (2016). *Car thefts decrease statewide*. East Bay Times. [URL](https://www.eastbaytimes.com/2007/02/16/car-thefts-decrease-statewide/)
