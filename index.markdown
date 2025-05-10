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
  ">4. What share of vehicles are involved in the crashes?</h2>
  <p style="font-size: 1.2rem; color: #3d1f23; line-height: 1.6;">Show top vehicle types involved in collisions using a pie or bar chart.</p>
</div>

<img src="/images/pieChartVehicleShare.png" alt="Top Vehicle Types in Collisions" style="width: 35vw; display: block; margin: auto; border-radius: 10px;" />

<div>
  <p>As we can see, the proportion</p>
</div>

<!-- SUV -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/suvContributingFactors.png" 
       alt="SUV Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p>Ayy Lmao</p>
</div>

<!-- Sedan -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/sedanContributingFactors.png" 
       alt="Sedan Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p style="text-align:center;">Ayy Lmao</p>
</div>

<!-- Bicycle -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/bikeContributingFactors.png" 
       alt="Bicycle Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
       <p>Ayy Lmao</p>
</div>

<!-- Motorcycle -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/motorbikeContributingFactors.png" 
       alt="Motorcycle Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
      <p>Ayy Lmao</p>
</div>
<!-- Van -->
<div class="image-block" style="margin-bottom: 40px;">
  <img src="/images/vanContributingFactors.png" 
       alt="Van Contributing Factors" 
       style="width: 40vw; display: block; margin: auto; border-radius: 10px;" />
  <p>Ayy Lmao</p>
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

[1] Sheppard, H. (2016). *Car thefts decrease statewide*. East Bay Times. [URL](https://www.eastbaytimes.com/2007/02/16/car-thefts-decrease-statewide/)

[2] Tsai, J. (2022). *One in three homes in this San Francisco neighborhood lives below the poverty line*. The San Francisco Standard. [URL](https://sfstandard.com/2022/12/08/san-francisco-neighborhood-new-census-data-maps/)

[3] Swan, Rachel, and Adriana Rezal. "These Neighborhoods Are San Francisco's Car-Theft Hot Spots." San Francisco Chronicle, San Francisco Chronicle, 28 Sept. 2023, [URL](https://www.sfchronicle.com/crime/article/car-theft-san-francisco-18387300.php)

[4] Kaplan, Ben. "2023 WE San Francisco Auto Theft Report." WE San Francisco, 1 Jan. 2024, www.wesanfrancisco.org/data/2023-car-theft. [URL](https://www.wesanfrancisco.org/data/2023-car-theft)