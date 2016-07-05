Title: Research

My research interets include large scale ocean circulation and its coupling effect with climate system, specifically the interaction between Agulhas leakage and the Atlantic Meridional Oerturning circulation.
<p align="center">
{% img http://www.saeon.ac.za/enewsletter/archives/2011/april2011/images/0402big.jpg 500 400 %}
</p>

####Motivation
The Agulhas current and its leakage of warm and salty indian-ocean water, play crucial role in the climate system by influencing Atlantic Meridional Overturning Circulation stability. While the ocean circulation models are not capable due to lacking of couplings, and the fully-coupled climate models fail because of inability to resolve mesoscale features, the high-resolution coupled model is the only viable tool to access this topic.

####Dataset
Due to limitation of computing resources, and the interests of longterm time-scale variabilities, current generation coupled-climate models are conventionally configured to horizontal resolution of 1.0 degree, and outputs are usuall stored monthly. This configuration leads to poor performances in simulating mesoscale features. In Agulhas current context, these models fail to reasonably simulate features such as Agulhas return current, Auglhas Ring, and therefore Agulhas leakage. Here, my work is based on a high-resolution configured Community Climate System Model (CCSM3.5) output. The spatial resolution of this simulation for the atmospheric and ocean component is 0.5 degree and 0.1 degree respectively. 

####Quantifying Agulhas leakage
The first difficulty we must overcome is quantifying Agulhas leakage robustly.In numerical models, where we have gridded data, a widely accepted approach to quantify Agulhas leakage is Lagrangian particle tracking. 

With the aid of Connectivity Modeling System (CMS), we release particles along the ACT array. Each particle is tagged with a volume flux equivalent to the local velocity times the corresponding grid cell size. They are advected by local velocity fields from CCSM3.5 forward in time for two years. Tracking every particle trajectories, we can determine whether one particle crossing the GoodHope line, which basin it ends up in, and, above all, the timing of last-crossing. Summing up the number of last-crossing particles of every time-step, we can establish time-series of Agulhas leakage. 
<p align="center">
{% video http://www.rsmas.miami.edu/users/ycheng/media/anim_p2d_r50.mp4 600 300 http://www.rsmas.miami.edu/users/ycheng/media/cover1.png %}</p>

####Temporal Resolution
The approach mentioned above is fairly simple; however, there are many technical diffculties we must solve. First, lagrangian calculations in previous studies are mostly based on [Ariane](http://stockage.univ-brest.fr/~grima/Ariane/) toolbox, which is not applicable to CCSM3.5 due to grid setup. Therefore, we use CMS instead. In addition, most of previos studies use Ocean General Circulation Model outputs with high temopral resolution (typically 5-daily output.), while most of Coupled Model outputs are archieved  monthly, which is not ideal for lagrangian particle tracking. 

To Adress these problems, we have tested different strategies, including releasing frequency, offshore boundary of releasing, particles with same the volume and so on. We also conducted several experiments using different temopral-resolution velocity fields to adress the degree of degradation of Agulhas leakage estimates of temporal-averaging.
<p align="center">
{% img http://www.rsmas.miami.edu/users/ycheng/media/AL_pent_vs_mon.png 1000 800 %}
</p>

####Future work
We've established a robust way to quantify Agulhas leakage in high-resolution CCSM3.5 output, with which we obtain much more resonable Agulhas Leakage estimates (~20Sv) than previous estimates based on coarse-resolution CCSM4 simulation. Our next plan is to apply such method to a complete 54year high-resolution pre-industrial CCSM3.5 run, and to a currently-running 20-Centuray climate change run to evaluate the variability of Agulhas leakage and possibliy to link such variability to other climate modes, such as El Niño, AMO and Indian Ocean Dipole. In particular, we are very interested in seeing the variability of Agulhas Leakage in the climate-change condition, because the inter-basin exchange is believed to counteract the global-warming effect on the AMOC.


