import styled from '@emotion/styled';

export const Container = styled.div`
  width: ${(props) => props.width};
`;

/**
 * storybook
 */
export const IconList = styled.ul`
  display: flex;
  padding: 0;
`;

export const IconItem = styled.li`
  width: 5rem;
  margin: 1rem;
`;
