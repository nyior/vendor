<template>
    <div class="wide-block">
        <h3>made with 💜 by</h3>
        <div class="featured-logo-row sub-heading">
            <span>
                Milton Doibo
            </span>
            <a 
                href="https://nyior-clement.netlify.app/"
                target="_blank">
                <span>
                    Nyior Clement
                </span>
            </a>
        </div>
    </div>
</template>
<script>
export default {
    name: "WideBlockFeatured"
};
</script>
<style scoped>
span{
    font-size: 4rem;
}
.wide-block {
    width: 100vw;
    height: 200px;
    margin-top: 30px;
    margin-bottom: 60px;
    display: flex;
    font-size: 2rem;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    position: relative;
}

.wide-block:after {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    content: "";
    width: 80px;
    height: 8px;
    background: rgba(0, 0, 0, 0.1);
    border-radius: 30px;
}
.wide-block .featured-logo-row {
    display: inline-flex;
    flex-direction: row;
    margin-top: 40px;
    gap: 50px;
}
.featured-logo-row img {
    height: 30px;
    filter: grayscale(100%);
}
.featured-logo-row img:hover {
    filter: none;
}

@media screen and (max-width: 640px) {
    .wide-block {
        margin-top: -100px;
    }
    .featured-logo-row {
        animation: scroll 20s linear infinite alternate;
    }

    span{
        font-size: 2rem;
        font-weight: bold;
    }
}

@keyframes scroll {
    0% {
        transform: translateX(-50%);
    }
    100% {
        transform: translateX(50%);
    }
}
</style>
