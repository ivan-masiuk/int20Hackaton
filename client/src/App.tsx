import { Container, useDisclosure } from '@chakra-ui/react';
import React from 'react'
import AppRouter from './components/AppRouter';
import Header from './components/Header';
import LoginModal from './components/modals/LoginModal';

const App: React.FC = () => {
	const isAuth = true;
	const { isOpen, onOpen, onClose } = useDisclosure()

	return (
		<Container maxW='container.xl'>
			<Header isAuth={isAuth} onLogin={onOpen}/>
			<AppRouter isAuth={isAuth} />
			<LoginModal isOpen={isOpen} onClose={onClose} />
		</Container>
	)
}

export default App
