<script lang="ts">
	let password: string = '';
	let confirmPassword: string = '';

	$: valid = password == confirmPassword || password == '' || confirmPassword == '';
</script>

<div
	class="flex flex-col w-full h-full bg-gradient-to-b from-oxford-blue-900 via-oxford-blue-500 to-zomp-900"
>
	<img class="h-12 mt-8 mb-4 mx-auto" src="/text_logo.png" alt="Ride Together Logo" />
	<form class="w-5/6 mx-auto" method="POST">
		{#if !valid}
			<p class="text-violet-red-800 text-xl p-2 mb-4 rounded-xl border-2 border-violet-red-800">Please ensure that your passwords match.</p>
		{/if}
		<div class="flex flex-row">
			<div class="w-full">
				<label for="firstName" class="text-baby-powder-50">First Name</label>
				<input
					id="firstName"
                    name="firstName"
					class="text-2xl w-full h-12 rounded-xl p-2 box-border"
					type="text"
					required
				/>
			</div>
			<div class="w-full ml-2">
				<label for="lastName" class="text-baby-powder-50 ">Last Name</label>
				<input
					id="lastName"
                    name="lastName"
					class="text-2xl w-full h-12 rounded-xl p-2 box-border"
					type="text"
					required
				/>
			</div>
		</div>
		<label for="username" class="text-baby-powder-50">Username</label>
		<input
			id="username"
            name="username"
			class="text-2xl w-full h-12 rounded-xl p-2 box-border"
			type="text"
			required
		/>

		<label for="email" class="text-baby-powder-50">Email</label>
		<input
			id="email"
            name="email"
			class="text-2xl w-full h-12 rounded-xl p-2 box-border"
			type="email"
			required
		/>

		<label for="password" class="text-baby-powder-50">Password</label>
		<input
			id="password"
            name="password"
			bind:value={password}
			class="text-2xl w-full h-12 rounded-xl p-2 box-border"
			type="password"
			required
		/>

		<label for="confirmPassword" class="text-baby-powder-50">Confirm Password</label>
		<input
			id="confirmPassword"
            name="confirmPassword"
			bind:value={confirmPassword}
			class="text-2xl w-full h-12 rounded-xl p-2 box-border"
			type="password"
			required
		/>
		<button
			class="my-4 py-4 mx-auto text-center w-full bg-oxford-blue-800 rounded-xl border-4 border-violet-red-600 text-baby-powder-50 text-2xl"
			disabled={!valid}
		>
			Register
		</button>
	</form>
	<a
		class="my-4 py-4 mx-auto text-center w-5/6 bg-oxford-blue-800 rounded-xl border-4 border-violet-red-600 text-baby-powder-50 text-2xl"
		href="/"
	>
		Cancel
	</a>
</div>
