<script lang="ts">

</script>

<div class="flex flex-col w-full h-full bg-gradient-to-b from-oxford-blue-900 via-oxford-blue-500 to-zomp-900">
    <img class="h-12 my-8 mx-auto" src="/text_logo.png" alt="Ride Together Logo"/>
    <form class="w-2/3 mx-auto" method="POST">
        <label for="username" class="text-baby-powder-50">Username</label>
        <input id="username" name="username" class="text-2xl w-full h-12 rounded-xl p-2 box-border" type="text">

        <label for="password" class="text-baby-powder-50">Password</label>
        <input id="password" name="password" class="text-2xl w-full h-12 rounded-xl p-2 box-border" type="password">
        <button class="my-4 py-4 mx-auto text-center w-full bg-oxford-blue-800 rounded-xl border-4 border-violet-red-600 text-baby-powder-50 text-2xl">
            Login
        </button>
    </form>
    <a class="my-4 py-4 mx-auto text-center w-2/3 bg-oxford-blue-800 rounded-xl border-4 border-violet-red-600 text-baby-powder-50 text-2xl" href="/">
        Cancel
    </a>
</div>