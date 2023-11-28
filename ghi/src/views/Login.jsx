import { useState } from 'react';
import { useLoginMutation, useGetTokenQuery } from '../store/authApi';

function Login() {
	const [username, setUsername] = useState('');
	const [password, setPassword] = useState('');
	const { data: account } = useGetTokenQuery();
	const [login, result] = useLoginMutation();

	const handleSubmit = (e) => {
		e.preventDefault();
		login({ username, password });
		console.log('Result of Login: ', result);
		e.target.reset();
	};

	return (
		<div>
			<h1>Login</h1>
			{account && <p>Welcome, {account.account.name}</p>}

			<form onSubmit={handleSubmit}>
				<label htmlFor="username">username</label>
				<input
					onChange={(e) => setUsername(e.target.value)}
					type="text"
					name="username"
					value={username}
					placeholder="username"
					id="username"
					required
				/>

				<label htmlFor="password">Password</label>
				<input
					onChange={(e) => setPassword(e.target.value)}
					type="text"
					name="password"
					value={password}
					placeholder="password"
					id="password"
					required
				/>
				<button type="submit">Login</button>
			</form>
		</div>
	);
}

export default Login;

/*
alt. login

import { useState } from 'react';
import { useAuthContext } from '@galvanize-inc/jwtdown-for-react';
import useToken from '@galvanize-inc/jwtdown-for-react';

const { login } = useToken();
const [username, setUsername] = useState('');
const [password, setPassword] = useState('');

const handleSubmit = (e) => {
	e.preventDefault();
	login(username, password);
	e.target.reset();
};
	<div className="card-body">
		<form onSubmit={(e) => handleSubmit(e)}>
			<div className="mb-3">
				<label className="form-label">Username:</label>
				<input
					name="username"
					type="text"
					className="form-control"
					onChange={(e) => setUsername(e.target.value)}
				/>
			</div>
			<div className="mb-3">
				<label className="form-label">Password:</label>
				<input
					name="password"
					type="password"
					className="form-control"
					onChange={(e) => setPassword(e.target.value)}
				/>
			</div>
			<div>
				<input className="btn btn-primary" type="submit" value="Login" />
			</div>
		</form>
	</div>
*/
