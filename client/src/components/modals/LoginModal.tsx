import { Button, FormControl, FormLabel, Input, InputGroup, InputRightElement, Modal, ModalBody, ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Stack } from '@chakra-ui/react'
import React, { useState } from 'react'

interface LoginModalProps {
	isOpen: boolean,
	onClose: () => void,
}

const LoginModal: React.FC<LoginModalProps> = ({ isOpen, onClose }) => {
	const [showPassword, setShowPassword] = useState(false);

	const handleShowClick = () => setShowPassword(!showPassword);

	return (
		<Modal isOpen={isOpen} onClose={onClose} isCentered>
			<ModalOverlay />
			<ModalContent>
				<ModalHeader fontSize={"2xl"}>Увійти</ModalHeader>
				<ModalCloseButton />
				<ModalBody>
					<Stack spacing={4}
						p=".5rem">
						<FormControl>
							<FormLabel>E-mail </FormLabel>
							<InputGroup>
								<Input type="email" />
							</InputGroup>
						</FormControl>
						<FormControl>
							<FormLabel>Пароль</FormLabel>
							<InputGroup>
								<Input
									type={showPassword ? "text" : "password"}
								/>
								<InputRightElement width="4.5rem">
									<Button h="1.75rem" size="sm" onClick={handleShowClick}>
										{showPassword ? "Hide" : "Show"}
									</Button>
								</InputRightElement>
							</InputGroup>
						</FormControl>
					</Stack>
				</ModalBody>


				<ModalFooter>
					<Button size={'md'} colorScheme="blue" w={"100%"}>Увійти</Button>
				</ModalFooter>
			</ModalContent>
		</Modal>
	)
}

export default LoginModal
