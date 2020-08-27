<template>

	<div class="my-footer text-center shadow  hide-on-desktop py-4">
		
		<div class="row m-2 text-muted">

			<div class="col-2" >
				<router-link :to="{ name: 'home' }" v-on:click="addActiveClass" class="footer-tab  active">
					<div>
						<i class="fa fa-window-maximize footer-icon"></i>
					</div>
					
					<div class="mt-1">
						<small>Home</small>
					</div>
				</router-link>
			</div>

			<div class="col-2" >
				<router-link :to="{ name: 'search' }" v-on:click="addActiveClass" class="footer-tab  ">
					<div>
						<i class="fa fa-search footer-icon"></i>
					</div>
					
					<div class="mt-1">
						<small>Search</small>
					</div>
				</router-link>
			</div>

			<div class="col-4" >
				<router-link :to="{ name: 'ads_create' }" v-on:click="addActiveClass" class="footer-tab ">
					<div>
						<i class="fa fa-plus-circle footer-icon"></i>
					</div>
					
					<div class="mt-1">
						<small>Sell</small>
					</div>
				</router-link>
			</div>

			<div class="col-2" >
				<router-link :to="{ name: 'wishlist' }" v-on:click="addActiveClass" class="footer-tab ">
					<div>
						<i class="fa fa-gratipay footer-icon"></i>
					</div>
					
					<div class="mt-1">
						<small>Wishlist</small>
					</div>
				</router-link>
			</div>

			<div class="col-2">
				<router-link :to="{ name: 'home' }" v-on:click="addActiveClass" class="footer-tab ">
					<div>
						<i class="fa fa-user-circle footer-icon"></i>
					</div>
					
					<div class="mt-1">
						<small>Profile</small>
					</div>
				</router-link>
			</div>

		</div>

	</div> 

</template>

<script>

  export default {
    name: "Footer",

	methods: {

		addActiveClass() {

			let footerTabsList = document.getElementsByClassName("footer-tab")

			for (let index = 0; index < footerTabsList.length; index++) {
				if (this == footerTabsList[index]){
					
					if (!this.classList.contains('active')) {
						this.classList.add('active');
					}

				}else{

					if (footerTabsList[index].classList.contains('active')) {
						footerTabsList[index].classList.remove('active');
					}
				}				
			}
		}
	}

    
  };

</script>

<style scoped>

.my-footer {
  font-size: 1.4rem;
  letter-spacing: 1px;
  width: 100%;
  
  background-color: white ;
  position: fixed;
  bottom: 0px;
  
}

.footer-icon{
	font-size: 2rem;	
}

.active{
	color: #7a09c4 !important;
}

ul li {
  margin: 0rem 1.5rem;
}
</style>
