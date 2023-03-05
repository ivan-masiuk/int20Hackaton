import React from 'react'
import { Navigate, Route, Routes } from "react-router-dom";
import { AppRoutes } from '../helpers/consts';
import { privateRoutes, publicRoutes } from '../routes';
import PrivateRoute from './PrivateRoute';

interface AppRouterProps {
	isAuth: boolean,
}


const AppRouter: React.FC<AppRouterProps> = ({ isAuth }) => {

	return (
		<Routes>
			{
				isAuth && privateRoutes.map(
					({ path, Component }) =>
						<Route
							key={path}
							path={path}
							element={
								<PrivateRoute isAuth={isAuth}>
									<Component />
								</PrivateRoute>
							}
						/>
				)
			}

			{publicRoutes.map(
				({ path, Component }) => <Route key={path} path={path} element={<Component />} />
			)}

			<Route path="*" element={<Navigate to={AppRoutes.HOME} replace />} />
		</Routes>
	)
}

export default AppRouter
