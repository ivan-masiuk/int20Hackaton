import { SearchIcon } from '@chakra-ui/icons';
import { Avatar, Badge, Box, Button, IconButton, Image, Input, InputGroup, InputRightElement, Text } from '@chakra-ui/react'
import React from 'react'
import { Link } from 'react-router-dom';
import Logo from "../assets/images/logo.svg"
import { AppRoutes } from '../helpers/consts';

interface HeaderProps {
	isAuth: boolean,
	onLogin: () => void,
}


const Header: React.FC<HeaderProps> = ({ isAuth, onLogin }) => {

	return (
		<Box display={'flex'}
			gap={'12'}
			justifyContent={"space-between"}
			alignItems={'center'}
			paddingY={'3'}
		>
			<Link to={AppRoutes.HOME}><Image src={Logo} w={'2xs'} /></Link>
			{isAuth
				? <>
					<InputGroup w={'full'}>
						<Input size="md"
							variant="outline"
							placeholder="Знайти проект"
						/>
						<InputRightElement>
							<IconButton
								aria-label='Пошук проектів'
								icon={<SearchIcon />}
							/>
						</InputRightElement>
					</InputGroup>
					<Box
						display={"flex"}
						alignItems={"center"}
						gap={'3'}
						flexShrink={0}
					>
						<Avatar
							src='https://chakra-ui.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F6916170%3Fv%3D4&w=96&q=75'
							maxW={12}
							borderRadius={'full'}
							mb={1}
						/>
						<Box>
							<Text fontSize={'xl'} fontWeight={'bold'}>Іванов Іван</Text>
							<Badge
								paddingX={'3'}
								paddingY={'1'}
								variant={"outline"}
								colorScheme={"green"}
								borderRadius={'7'}
							>
								JavaScript / Front-End
							</Badge>
						</Box>
					</Box>
				</>
				: <Button
					size={"md"}
					colorScheme={"blue"}
					variant={'outline'}
					onClick={onLogin}
				>
					Увійти до аккаунту
				</Button>
			}
		</Box>
	)
}

export default Header
