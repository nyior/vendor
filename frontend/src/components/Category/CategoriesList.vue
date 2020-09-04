<template>

  <div class="mt-5 ">

     <ul class="list-unstyled list-inline">

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'adverts'}"
            >
              
              <div class=" text-muted">
                
                <strong>ALL</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Fashion' } }"
            >
              
              <div class=" text-muted">
                
                <strong>FASHION</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Electronic Appliances' } }"
            >
              
              
              <div class=" text-muted">
                
                <strong>ELECTRONIC APPLIANCES</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Phones and Accessories' } }"
            >
              
             
              <div class=" text-muted">
                
                <strong>PHONES AND ACCESSORIES</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Video Games' } }"
            >
              
            
              <div class=" text-muted">
                <strong>VIDEO GAMES</strong>
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Services' } }"
            >
              
              <div class=" text-muted">
                
                <strong>SERVICES</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Health and Beauty' } }"
            >
              
              
              <div class=" text-muted">
                
                <strong>HEALTH AND BEAUTY</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item border-right p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Foods' } }"
            >
              
              
              <div class=" text-muted">
                
                <strong>FOODS</strong>
                
              </div>
            </router-link> 
        </li> 

        <li class="list-inline-item  p-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Others' } }"
            >
              
             
              <div class=" text-muted">
                
                <strong>OTHERS</strong>
                
              </div>
            </router-link> 
        </li> 

     </ul>

  </div>
  
</template>

<script>

  export default {

    name: "categories-list",
  
  };

</script>

<style scoped>

</style>
