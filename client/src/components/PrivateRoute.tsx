import React from 'react'
import { Navigate, RouteProps } from 'react-router-dom'
import { AppRoutes } from '../helpers/consts'

interface PrivateRouteProps {
	isAuth: boolean,
	children: React.ReactNode
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({ isAuth, children }) => {

	if (!isAuth) {
		return <Navigate to={AppRoutes.AUTH} replace />;
	}

	return <>{children}</>
}

export default PrivateRoute
