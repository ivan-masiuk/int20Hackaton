import { ArrowBackIcon } from '@chakra-ui/icons'
import { Avatar, Badge, Box, Button, Heading, Image, Stack, Tag, Text } from '@chakra-ui/react'
import React from 'react'
import { Link } from 'react-router-dom'
import Layout from '../components/Layout'
import { AppRoutes } from '../helpers/consts'

const Project: React.FC = () => {

	const team = [
		{
			name: 'Vlad',
			role: 'Frontend',
			avatar: 'https://chakra-ui.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F6916170%3Fv%3D4&w=96&q=75'
		},
		{
			name: 'Vlados',
			role: 'Backend',
			avatar: 'https://chakra-ui.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F6916170%3Fv%3D4&w=96&q=75'
		},
	]

	const searchingRoles = ["JavaScript / Front-End ", "Python / Back-End"]

	const isOwner = true;


	const teamItems = team.map((item, index) =>
		<Box
			display={"flex"}
			alignItems={"center"}
			gap={'3'}
			flexShrink={0}
			key={index}
		>
			<Avatar
				src={item.avatar}
				maxW={12}
				borderRadius={'full'}
				mb={1}
			/>
			<Box>
				<Text fontSize={'xl'} fontWeight={'bold'}>{item.name}</Text>
				<Badge
					paddingX={'3'}
					paddingY={'1'}
					variant={"outline"}
					colorScheme={"blue"}
					borderRadius={'7'}
				>
					{item.role}
				</Badge>
			</Box>
		</Box>
	)


	return (
		<Layout>
			<Box display={'flex'} alignContent="center" justifyContent="space-between">
				<Link to={AppRoutes.HOME}>
					<Button size={'md'}
						variant="outline"
						leftIcon={<ArrowBackIcon />}
						mb={'4'}
					>
						Повернутись до списку
					</Button>
				</Link>
				{isOwner
					? <Box display={"flex"}  alignItems="center" gap={4}>
						<Text>Кількість заявок: 5</Text>
						<Button colorScheme={'green'}>Переглянути</Button>
					</Box>
					: null
				}

			</Box>
			<Box display={'flex'} gap="4">
				<Stack spacing={4} flexShrink={0} flexBasis="400px">
					<Image src="https://via.placeholder.com/400x300" mb={'3'} />
					<Box>
						<Text mb="3" fontWeight={500} fontSize={'xl'}>Вже в команді</Text>
						<Stack spacing="5">
							{teamItems}
						</Stack>
					</Box>
					<Box>
						<Text mb="3" fontWeight={500} fontSize={'xl'}>Шукаємо</Text>
						<Stack spacing="5" alignItems={'flex-start'}>
							{searchingRoles.map((role, index) => <Tag key={index} colorScheme="blue" size={'lg'}>{role}</Tag>)}
						</Stack>
					</Box>
				</Stack>

				<Box>
					<Heading mb="4">Project on python </Heading>
					<Text mb="4">
						RetroVerse is a web-based platform that connects gamers from around the world who love playing retro video games. The platform allows users to create profiles, join groups, and participate in events and tournaments centered around classic video games. RetroVerse aims to bring back the nostalgia of retro gaming and provide a community for those who share the same passion. The platform will generate revenue through a subscription-based model, which grants users access to premium features such as exclusive game content and early access to events and tournaments.
						We are currently looking for team members with experience in web development, community management, and marketing to help bring RetroVerse to life. If you share our love for retro gaming and are interested in joining our team, please reach out to us!
					</Text>
					<Button mb="4" size="md" colorScheme={'blue'}>
						Стати учасником проєкту
					</Button>
				</Box>
			</Box>

		</Layout>
	)
}

export default Project
