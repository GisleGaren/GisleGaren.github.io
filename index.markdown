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
      <a href="#what-hits-javi" style="color: black;">
        <strong>4. 🚗</strong> What Hits Javi?
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#who-gets-hurt" style="color: black;">
        <strong>5. 🤕</strong> Who Gets Hurt?
      </a>
    </li>
    <li style="margin-bottom: 8px;">
      <a href="#dangerous-combos" style="color: black;">
        <strong>6. ⚠️</strong> Most Dangerous Combos
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



<div id="intro-javi" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>1. Introduction: Meet Javi</h2>
  <p>Short story: Javi is a delivery driver in NYC, navigating a city full of risks. This sets up the context for your visual storytelling.</p>
</div>

# Add your plot here

<div id="dangerous-hours" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>2. Dangerous Hours</h2>
  <p> The interactive bar chart visualizes the frequency of vehicle collisions involving Uber drivers in New York City, broken down by hour of the day and day of the week. 
  Each hour from midnight (00:00) to 11 PM (23:00) is shown along the x-aksis and the y-axis represents the total number of recorded collisions. The bars are grouped and color-coded by day of the week, helping highlight temporal patterns in collision risk. </p>

</div>

# Add your plot here 

<iframe 
    src="/assets/dangerous_hours_plot.html" 
    width="1000" 
    height="700"
    frameborder="0"
    scrolling="no"
></iframe>

<div>
  Collisions peaks tend to occur during rush hours (7-9 AM and 4-7 PM), especially on weekdays. Fridays often show higher evening collisions, likely due to increased ride demand and traffic congestion. On weekends, while overall low, some late-night risks are tied to nightlife hours (1-3 AM).
</div>
 

<div id="dangerous-places" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>3. Dangerous Places</h2>
  <p>Interactive Map of Collision Locations like the one we had in assignment 2.</p>
</div>

# Add your plot here

<div id="what-hits-javi" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>4. What Hits Javi?</h2>
  <p>Show top vehicle types involved in collisions using a pie or bar chart.</p>
</div>

# Add your plot here

<div id="who-gets-hurt" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>5. Who Gets Hurt?</h2>
  <p>Charts to explore injury demographics by age, sex, and transport mode (pedestrian, cyclist, etc).</p>
</div>

# Add your plot here

<div id="dangerous-combos" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>6. Most Dangerous Combos</h2>
  <p>Pairings like “Taxis injure cyclists most between 6–9pm.” Consider using a story tableau with filtered charts.</p>
</div>

# Add your plot here

<div id="conclusion" style="margin-top: 8vh; margin-bottom: 5vh; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 2px 1px rgb(0 0 0 / 40%)">
  <h2>7. Conclusion: Can Javi Make It?</h2>
  <p>Summarize patterns to offer takeaways like avoiding certain hours or locations.</p>
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