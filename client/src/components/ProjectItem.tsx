import { AspectRatio, Box, Heading, HStack, Image, Stack, Tag, Text } from '@chakra-ui/react'
import React from 'react'
import { Link } from 'react-router-dom'
import { AppRoutes } from '../helpers/consts'
import { IProjectItem } from '../models/IProjectItem'

interface ProjectItemProps extends IProjectItem {
}

const ProjectItem: React.FC<ProjectItemProps> = ({ id, images, title, users, search_for }) => {


	const getRolesTags = (users: any) => {
		return users.map((user: any, idx: number) => <Tag key={idx} size={"lg"} colorScheme="blue" variant={"outline"}>{user.role.name}</Tag>)
	}


	return (

		<Box border={'1px'} borderColor="gray.200" rounded={'md'} >
			<Link to={`${AppRoutes.PROJECT}/${id}`}>
				<AspectRatio ratio={3 / 2} mb="10px">
					<Image borderTopRadius={'md'} src={images} alt={`Cover of ${title}`} />
				</AspectRatio>
				<Box paddingX={'14px'} paddingBottom="20px">
					<Heading size={'lg'} mb="5px"> {title} </Heading>
					<Stack spacing={3}>
						<Box>
							<Text size={'xs'} mb={"1"} fontWeight={'500'}>Вже в команді</Text>
							<Box display={'flex'} flexWrap="wrap" gap={1.5}>{getRolesTags(users)} </Box>
						</Box>
						<Box>
							<Text size={'xs'} mb={"1"} fontWeight={'500'}>Шукаємо</Text>
							<Box display={'flex'} flexWrap="wrap" gap={1.5}>{getRolesTags(search_for)} </Box>
						</Box>
					</Stack>
				</Box>
			</Link>
		</Box>

	)
}

export default ProjectItem



